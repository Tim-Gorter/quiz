
from googleapiclient.discovery import build
import googleapiclient.http
import os
from googleapiclient.discovery import build
import random
import io
import time
import numpy as np
import logging
import datetime
import threading


class GoogleDrive:    
        def __init__(self, visualManager=None):      
            self.drive_service = build('drive', 'v3')
            self.folderid = '1c8V2zmEV3GJbOiKT6z61LkZyS8cIPDPE'
            self.userid = None
            self.userid = self.register()
            self.get_performances()
            self.visualManager = visualManager
            logging.getLogger("google_auth_httplib2").setLevel(logging.ERROR)

        def update_status(self, text):
            self.visualManager.download_status.value = text

        def _json_safe(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.floating):
                return float(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            
            return str(obj)

        def get_folder(self, userid):
            query = f"name='{userid}' and '{self.folderid}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
            max_retries = 5
            # it can take some time for the folder to get registered
            for attempt in range(max_retries):
                results = self.drive_service.files().list(q=query, fields="files(id)").execute()
                files = results.get('files', [])

                if files:
                    return files[0]['id']
                    time.sleep(2 ** attempt)

        def download(self, file_id, file_name, userid):
            request = self.drive_service.files().get_media(fileId=file_id)

            #create the userid folder if not existing
            path = os.path.join("drive", str(userid))
            os.makedirs(path, exist_ok=True)

            file_path = os.path.join(path, file_name)

            fh = io.FileIO(f"{file_path}", 'wb')
            downloader = googleapiclient.http.MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()

        def get_performances(self):
            folderid = self.get_folder(self.userid)
            query = f"'{folderid}' in parents and trashed=false"
            results = self.drive_service.files().list(q=query, fields="files(id, name)").execute()
            files = results.get('files', [])

            if not os.path.exists('/content/drive/' + str(self.userid)):
                os.makedirs('/content/drive/' + str(self.userid))

            for file in files:
                if not os.path.exists('./drive/' + str(self.userid) + '/' + file['name']):
                    self.download(file['id'], file['name'], self.userid)

        def get_performances_master(self):
            query = f"'{self.folderid}' in parents and trashed=false"
            results = self.drive_service.files().list(q=query, fields="files(id, name)").execute()
            folders = results.get('files', [])

            total_files = sum(
                len(self.drive_service.files().list(q=f"'{folder['id']}' in parents and trashed=false",
                                                    fields="files(id)").execute().get('files', []))
                for folder in folders
            )
            downloaded_files = 0

            save_path = '/content/drive/'
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            for folder in folders:
                if not os.path.exists(os.path.join(save_path, folder['name'])):
                    os.makedirs(os.path.join(save_path, folder['name']))
                query = f"'{folder['id']}' in parents and trashed=false"
                results2 = self.drive_service.files().list(q=query, fields="files(id, name, modifiedTime)").execute()
                files = results2.get('files', [])
                for file in files:
                    download_file = False
                    file_location = os.path.join(save_path,folder['name'], file['name'])
                    if os.path.exists(file_location):
                        #already exists, check if it needs to be updated
                        last_edited_local = datetime.fromtimestamp(os.path.getmtime(file_location))
                        last_edited_drive = datetime.fromisoformat(file['modifiedTime'].replace('Z', '+00:00')).replace(tzinfo=None)
                        if last_edited_local < last_edited_drive:
                            download_file = True
                    else:
                        #File does not exist yet
                        download_file = True
                    if download_file:
                        # self.download(file['id'], file['name'], folder['name'])
                        threading.Thread(target=self.download(file['id'], file['name'], folder['name'])).start()


                    downloaded_files += 1
                    self.update_status(f"Download status: {downloaded_files}/{total_files} files downloaded")

            self.update_status("Download finished")

        def login_correct(self,userid):
            query = f"name='{userid}' and '{self.folderid}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
            results = self.drive_service.files().list(q=query, fields="files(id)").execute()
            if len(results['files']) > 0:
                return True
            else:
                return False

        def register(self):
            if self.userid !=None:
                return self.userid

            query = f"'{self.folderid}' in parents and mimeType='application/vnd.google-apps.folder' and trashed = false and 'me' in owners"
            results = self.drive_service.files().list(q=query,pageSize=1000,fields='files(id, name)').execute()
            files = results.get('files', [])

            if len(files) > 0:
                return files[0]['name']
            else:
                userid = None
                while True:
                    userid = str(random.randint(10000, 99999))
                    query2 = f"name='{userid}' and '{self.folderid}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
                    results2 = self.drive_service.files().list(q=query2,pageSize=1000,fields="files(name)").execute()
                    files2 = results2.get('files', [])
                    if len(files2) > 0:
                        continue
                    else:
                        file_metadata = {
                        'name': userid,
                        'mimeType': 'application/vnd.google-apps.folder',
                        'parents': [self.folderid]
                        }
                        file = self.drive_service.files().create(body=file_metadata, fields='id').execute()
                        self.userid = userid
                        return userid


        def to_serializable(self, obj):
            if isinstance(obj, np.generic):
                return obj.item()
            elif isinstance(obj, dict):
                return {k: self.to_serializable(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [self.to_serializable(v) for v in obj]
            elif isinstance(obj, tuple):
                return tuple(self.to_serializable(v) for v in obj)
            else:
                return obj


        def write_answer_to_file(self, answer, filename):
            import json
            with open(f"./drive/{self.userid}/{filename}", "w", encoding="utf-8") as f:
                json.dump(answer, f, ensure_ascii=False, indent=4, default=self._json_safe)

        def upload_log(self, filename):
            folderid = self.get_folder(self.userid)

            #see if the file already exists
            query = f"name='{filename}' and '{folderid}' in parents and trashed = false"
            response = self.drive_service.files().list(q=query, spaces='drive', fields='files(id)').execute()
            files = response.get('files', [])

            media = googleapiclient.http.MediaFileUpload('./drive/'+ str(self.userid) + '/' + filename, mimetype="application/json", resumable=True)

            if files:
                #file already exists, overwrite
                file_id = files[0]['id']
                uploaded_file = self.drive_service.files().update(
                    fileId=file_id,
                    media_body=media
                ).execute()
            else:
                #file does not exist yet, create
                file_metadata = {
                "name": filename,
                "parents": [folderid]
                }

                uploaded_file = self.drive_service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields="id"
                ).execute()

            def set_userid(self,userid):
                self.userid = userid
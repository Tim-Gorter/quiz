import os
import random
from datetime import datetime

class GoogleDrive():
    def __init__(self):
       self.userid = 123
    def login_correct(self,userid):
        if userid == '':
           return False
        
        if os.path.isdir('./drive/' + userid):
           return True
        else:
           return False
        
    def upload_log(self, question):
       None
       #no need to upload, as it is already local

    def get_performances(self, userid):
       None
       #This function is not neccesary for the local drive, since the files are already stored locally
    
    def register(self):
      folders = set(os.listdir('./drive'))
      userid = None
      while True:
         userid = str(random.randint(10000, 99999))
         if userid not in folders:
            os.makedirs('./drive/' + userid)
            break
      return userid
    def write_answer_to_file(self, answer, filename):
        import json
        with open(f"./drive/{self.userid}/{filename}", "w", encoding="utf-8") as f:
            json.dump(answer, f, ensure_ascii=False, indent=4)
      
      
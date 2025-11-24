from datetime import datetime
import io
from IPython.display import clear_output,HTML, display
from ipytree import Tree, Node
from ipywidgets import *
import warnings
import os
import sys
import subprocess

class MLDashboard:
    def __init__(self,drive, online_version):
        self.clone()
        sys.path.append("components/MLDashboardComponent")
        os.chdir("./components/MLDashboardComponent")
        from controller.controller import Controller
        self.controller = Controller(drive, online_version)
        
    def get_ui(self):
        ui = self.controller.get_ui()
        return ui
    
    def clone(self):
        target_dir = "components/MLDashboardComponent"

        try:
            result = subprocess.run(
                ["git", "clone", "https://github.com/muratfirat78/ML_Dashboard", target_dir],
                capture_output=True, text=True, check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(e.stderr)
from datetime import datetime
import io
from IPython.display import clear_output,HTML, display
from ipytree import Tree, Node
from ipywidgets import *
import warnings
import os
import sys

class MLDashboard:
    def __init__(self,drive, online_version):
        !git clone https://github.com/muratfirat78/ML_Dashboard components/MLDashboardComponent
        sys.path.append("components/MLDashboardComponent")
        os.chdir('./components/MLDashboardComponent')
        from components.MLDashboardComponent.controller.controller import Controller
        self.controller = Controller(drive, online_version)
        
    def get_ui(self):
        ui = self.controller.get_ui()
        return ui
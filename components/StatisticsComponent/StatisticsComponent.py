from ipywidgets import *
from .Visual import *

class StatisticsComponent():
    def __init__(self, visualmanager):
        self.visualManager = visualmanager
        None
        
    def get_ui(self):
        VisManager = VisualManager(self.visualManager)
        tab = VisManager.generateHTTab()
        return tab

from QuestionsList import QuestionsList
import ipywidgets as widgets
from IPython.display import display

class SelectComponent:
    def __init__(self, visualManager):
        self.visualManager = visualManager
        questionlist = QuestionsList()
        self.component_list = widgets.Dropdown(
            options=questionlist.get_components(),
            disabled=False
        )
        
        self.start_button = widgets.Button(
            description="Start",
            button_style="success", 
            icon="play"
        )
        self.start_button.on_click(self.start_quiz)
        
        self.vbox = widgets.VBox([self.component_list, self.start_button])

    def get_ui(self):
        return self.vbox
    
    def hide(self):
        self.component_list.layout.display = "none"
        self.start_button.layout.display = "none"
        
    
    def start_quiz(self, value):
        self.visualManager.start_quiz(self.component_list.value)
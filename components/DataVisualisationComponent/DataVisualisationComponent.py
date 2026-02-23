import ipywidgets as widgets
import os
class DataVisualisationComponent():
    def __init__(self, visualmanager, columns, image_name):
        self.visualManager = visualmanager
        self.columns = columns
        self.image_name = image_name
        self.dataType = {}
        self.current_field = self.columns[0]
        self.fields = None
        self.datatype = None
        self.marks = None
        self.pos = None
        self.size = None
        self.color = None
        self.submit_button = None

        self.marks = None
        self.size = None
        self.color = None
        self.position = None
        
        for column in self.columns:
            self.dataType[column] = [None, None]

    def on_change(self):
        datatype = self.datatype.value
        position = self.pos.value
        self.dataType[self.current_field] = [datatype, position]
    
    def on_change_field(self, change):
        self.current_field = change['new']
        
        values = self.dataType.get(self.current_field, [None, None])
        self.datatype.value = values[0]
        self.pos.value = values[1]
    
    def on_submit(self, change):
        answer_obj = {}
        answer_obj["type"] = "custom"
        answer_obj["answer"] = {}
        for key in self.dataType.keys():
            datatype = self.dataType[key]
            answer_obj["answer"][key + "-datatype"] = datatype[0]
            answer_obj["answer"][key + "-position"] = datatype[1]

        answer_obj["answer"]["marks"] = self.marks.value
        answer_obj["answer"]["size"] = self.size.value
        answer_obj["answer"]["color"] = self.color.value
        

        self.visualManager.submit_answer(answer_obj)

    def get_ui(self):
        self.fields = widgets.Select(
            options=self.columns,
            description='',
            layout=widgets.Layout(width='150px', height='60px')
        )

        self.datatype = widgets.RadioButtons(
            options=['Nominal', 'Ordinal', 'Numerical'],
            value=None,
            layout=widgets.Layout(width='150px')
        )

        self.marks = widgets.RadioButtons(
            options=['Points', 'Lines', 'Areas'],
            value=None,
            description='Marks:',
            layout=widgets.Layout(width='150px')
        )

        self.pos = widgets.RadioButtons(
            options=['X Position', 'Y Position'],
            value=None,
            layout=widgets.Layout(width='150px')
        )
        self.size = widgets.RadioButtons(
            options=['Length', 'Area', 'Volume'],
            value=None,
            layout=widgets.Layout(width='150px')
        )
        self.color = widgets.RadioButtons(
            options=['Luminance', 'Hue'],
            value=None,
            layout=widgets.Layout(width='150px')
        )
        self.submit_button = widgets.Button(
            description="Submit",
        )
        self.submit_button.on_click(self.on_submit)

        #observers
        self.fields.observe(lambda change: self.on_change_field(change), names='value')
        self.datatype.observe(lambda change: self.on_change(), names='value')
        self.pos.observe(lambda change: self.on_change(), names='value')

        file = open("./components/DataVisualisationComponent/images/" + self.image_name, "rb")
        image_file = file.read()
        image = widgets.Image(
            value=image_file,
            format='png',
            width=600,
            height=300
        )

        top_row = widgets.HBox([self.fields, self.datatype])
        marks_row = widgets.HBox([self.marks])
        channels_row = widgets.HBox([
            widgets.VBox([widgets.Label("Position"), self.pos]),
            widgets.VBox([widgets.Label("Size"), self.size]),
            widgets.VBox([widgets.Label("Color"), self.color])
        ])

        ui = widgets.HBox([widgets.VBox([
            top_row,
            widgets.Label(""),
            marks_row,
            widgets.Label("Channels"),
            channels_row,
            self.submit_button
        ]), image ])

        return ui


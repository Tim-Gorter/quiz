class Question():
    def __init__(self, title, text,mchoice, component, parameters=None):
        self.title = title
        self.text = text
        self.type = mchoice
        self.choices = []
        self.tests = []
        self.keywords = []
        self.correctchoice = None
        self.component = component
        self.parameters = parameters

    def getTitle(self):
        return self.title

    def getText(self):
        return self.text

    def getChoices(self):
        return self.choices

    def getCorrectChoice(self):
        return self.correctchoice

    def setChoices(self,myit):
        self.choices = myit
        return

    def setTests(self,tests):
        self.tests = tests
        return

    def setKeywords(self,keywords):
        self.keywords = keywords
        return

    def IsMChoice(self):
        return self.type == 'multiple_choice'

    def isCustomQuestion(self):
        return self.type == 'custom'

    def isProgrammingQuestion(self):
        return self.type == 'programming'

    def isOpenQuestion(self):
        return self.type == 'open'

    def isInfo(self):
        return self.type == 'info'
    
    def get_component_name(self):
        return self.component
    
    def get_parameters(self):
        return self.parameters
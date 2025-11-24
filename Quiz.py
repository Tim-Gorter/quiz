import pandas as pd
from Question import Question
from QuestionsList import QuestionsList
class Quiz():
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.currentQuestion = None

    def getName(self):
        return self.name

    def getQuestions(self):
        return self.questions

    def setCurrentQuestion(self,myqst):
        self.currentQuestion = myqst
        return

    def getCurrentQuestion(self):
        return self.currentQuestion
    
    def open_quiz(tab_set, component):
        qtslist = []
        quizstr = "Quiz Deel 1_Questions"
        qname = quizstr[:quizstr.find("_Questions")]
        currentQuiz = Quiz(qname)
        url = ""
        if qname == "Quiz Deel 1":
            url = "https://github.com/muratfirat78/Python/raw/main/Quiz Deel 1_Questions.csv"

        url = url.replace(" ", "%20")
        Questions_df = pd.read_csv(url, sep=',')
        
        questionlist = QuestionsList()
        questions = questionlist.get_filtered_questions(component)

        for i in range(len(questions)):
            if questions[i]["type"] == "custom":
                component = questions[i]["component"]
                parameters = questions[i]["parameters"]
            else:
                component = None
                parameters = None

            newquestion = Question(questions[i]["title"],questions[i]["text"],questions[i]["type"], component, parameters)
            # newquestion = Question(r['Title'],r['Text'],r['Correctness'].find('~~')>-1)
            choices = questions[i]["choices"]
            correctness = questions[i]["correctness"]

            if newquestion.IsMChoice():
                for i in range(len(choices)):
                    newquestion.getChoices().append((choices[i],correctness[i]))
            else:
                newquestion.getChoices().append((questions[i]["choices"],questions[i]["correctness"]))

            currentQuiz.getQuestions().append(newquestion)
            
        return currentQuiz
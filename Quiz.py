import pandas as pd
from Question import Question
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
    
    def open_quiz(tab_set):
        qtslist = []
        quizstr = "Quiz Deel 1_Questions"
        qname = quizstr[:quizstr.find("_Questions")]
        currentQuiz = Quiz(qname)
        url = ""
        if qname == "Quiz Deel 1":
            url = "https://github.com/muratfirat78/Python/raw/main/Quiz Deel 1_Questions.csv"

        url = url.replace(" ", "%20")
        Questions_df = pd.read_csv(url, sep=',')

        questions = [{
            "title": "Question 1",
            "text": "Noem een voordeel en een nadeel van het feit dat Python dynamisch getypeerd is",
            "choices": "",
            "type":"open",
            "correctness":"Een voordeel is: type casting is niet nodig. Een nadeel is: fouten met betrekking tot typen worden er niet door een compiler uitgehaald; je komt ze pas tegen tijdens het draaien van een programma."
        },{
            "title": "Question 2",
            "text": "Bij elke waarde hoort één type? Welke van de uitspraken over deze stelling is juist?",
            "choices": ["De uitspraak geldt alleen voor dynamische typering.", "De uitspraak geldt alleen voor statische typering.", "De uitspraak geldt voor zowel statische als dynamische typering.", "De uitspraak heeft tot gevolg dat elke variabele een vast type heeft.","De uitspraak heeft niet tot gevolg dat elke variabele een vast type heeft."],
            "type":"multiple_choice",
            "correctness":[False,False,True,False,False]
        }
        ,{
            "title": "Question 3",
            "text": "Implementeer een functie square() die één parameter accepteert en het kwadraat van dat getal teruggeeft",
            "choices": "",
            "type":"programming",
            "correctness":{
                "tests": {"2":4,"3":9,"4":16},
                "keywords": ["for", "in", "print"],
                "function_name": "square"
                }
        }]

        for i in range(len(questions)):
            newquestion = Question(questions[i]["title"],questions[i]["text"],questions[i]["type"])
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
import pandas as pd
from Question import Question
from QuestionsList import QuestionsList
import os
import json
class Quiz():
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.currentQuestion = None

    def getName(self):
        return self.name

    def getQuestions(self):
        return self.questions
    
    def getQuestionsWithStatus(self, userid):
        questions_with_status = []
        for q in self.questions:
            status = self.get_question_status(q.getTitle(), userid) 
            label = f"{q.getTitle()}{status}" 
            value = q.getTitle()              
            questions_with_status.append((label, value))
        return questions_with_status
    
    def get_question_status(self,question_name, userid):
        answer_file = os.path.join("drive", str(userid), question_name + ".json")
        if not os.path.exists(answer_file):
            return ""  # no answer yet

        with open(answer_file, 'r', encoding='utf-8') as f:
            answer_data = json.load(f)

        if answer_data["type"] in ["multiple_choice", "open"]:
            if answer_data.get("result") == "correct":
                return "✅"
            elif answer_data.get("result") == "incorrect":
                return "❌"
            else:
                return ""

        if answer_data["type"] == "programming":
            correct_keywords = answer_data.get("correct_keywords", 0)
            total_keywords = answer_data.get("total_keywords", 0)

            result_data = answer_data.get("result", {})

            if result_data is None:
                return "❌"
            if not isinstance(result_data, dict):
                result_data = {}

            all_tests_passed = all(
                v.get("correct", False)
                for v in result_data.values()
                if isinstance(v, dict)
            )

            any_test_passed = any(
                v.get("correct", False)
                for v in result_data.values()
                if isinstance(v, dict)
            )

            if correct_keywords == total_keywords and all_tests_passed:
                return "✅"
            elif correct_keywords > 0 or any_test_passed:
                return "~"
            else:
                return "❌"

        return ""

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
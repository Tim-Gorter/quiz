from ipywidgets import *
from IPython.display import clear_output, display
from ProgrammingQuestion import ProgrammingQuestion
import importlib

class VisualManager():
    def __init__(self, drive, online_version):
        self.programmingQuestion = ProgrammingQuestion(online_version)
        self.online_version = online_version
        self.drive = drive
        self.userid_display = HTML(
            value=f"<b style='font-size:16px; color:black; background-color:#e0e0e0; padding:2px 4px; border-radius:3px;'>Your user is: {self.drive.userid}</b>"
        )
        self.Qname= widgets.Label(value="Questions")
        self.Qqsts= widgets.Select(description="")
        self.Qqsts.layout.width ='95%'
        self.Qqsts.observe(self.open_question)
        self.description_out = widgets.Output()
        self.feedback_out = widgets.Output()
        self.qans_lbl= widgets.Label(value="Answer:")
        self.qans_lbl.layout.visibility = 'hidden'
        self.qans_lbl.layout.display = 'none'
        self.writtenresp = widgets.Textarea(value='')
        self.writtenresp.layout.visibility = 'hidden'
        self.writtenresp.layout.display = 'none'
        self.component_output = widgets.Output()
        self.display_only_answer = widgets.HTML()
        self.display_only_answer.layout.visibility = 'hidden'
        self.display_only_answer.layout.display = 'none'
        self.choices = widgets.RadioButtons(options=[],description='',disabled=False)
        self.choices.layout.height = '150px'
        self.choices.layout.width = '99%'
        self.check = widgets.Button(description="Submit")
        self.check.on_click(self.check_selection)
        self.currentQuiz = None
        self.components_ui = {}

        #quiz tab
        hboxleft = VBox(children=[self.Qname,self.Qqsts],layout=Layout(width = '15%'))
        qvbox = VBox(children=[self.description_out,self.qans_lbl,self.writtenresp,self.display_only_answer,self.choices, self.component_output])

        hboxmiddle = VBox(children=[qvbox,HBox(children=[self.check],layout=Layout(align_items='stretch')),self.feedback_out],layout=Layout(width = '75%'))
        hboxright = HBox(children=[VBox(children=[])],layout=Layout(width = '15%'))

        self.QuizTab = VBox([self.userid_display,
                             HBox([hboxleft,hboxmiddle,hboxright])
                             ])
    def setQuiz(self, quiz):
        self.currentQuiz = quiz

    def getQsts(self):
        return self.Qqsts

    def getQuizTab(self):
        return self.QuizTab

    ############################################################################################################################################
    def get_autofill_answer(self,question_name):
      answer_file = os.path.join(os.path.join("drive", str(self.drive.userid)), question_name + ".json")
      if os.path.exists(answer_file):
          import json
          with open(answer_file, 'r', encoding='utf-8') as f:
              answer_data = json.load(f)

          if answer_data["type"] == "multiple_choice":
              return answer_data["answer"]
          elif answer_data["type"] == "open":
              return answer_data["answer"]
          elif answer_data["type"] == "programming":
            code_str = "".join(answer_data["answer"])
            html_output = f"<pre><code>{code_str}</code></pre>"
            return html_output

          return None

    def get_component_ui(self, component_name, question_name):
        saved_component_name = component_name + "_" + question_name
        if saved_component_name in self.components_ui:
            return self.components_ui[saved_component_name]
        else:
            component_path = f"components.{component_name}Component.{component_name}Component"
            class_name = f"{component_name}Component"
            module = importlib.import_module(component_path)
            component_class = getattr(module, class_name)
            component = component_class(self)
            ui = component.get_ui()
            self.components_ui[saved_component_name] = ui
            return ui   
    
    def open_question(self, b):
        BOLD = '\033[1m'
        RESET = '\033[0m'
        for qstn in self.currentQuiz.getQuestions():
            if qstn.getTitle() == self.Qqsts.value:
                self.currentQuiz.setCurrentQuestion(qstn)
                break

        if self.currentQuiz.getCurrentQuestion() is None:
           return

        try:
            Qtitle = self.currentQuiz.getCurrentQuestion().getTitle()
            QText = self.currentQuiz.getCurrentQuestion().getText()
            autofill_answer = self.get_autofill_answer(Qtitle)
            with self.description_out:
                clear_output(wait=True)
                print(f"""{BOLD}{Qtitle}{RESET}""")
                print("_______________________________")
                print(QText)
                print()

            if self.currentQuiz.getCurrentQuestion().IsMChoice():
                self.choices.layout.display = 'block'
                self.choices.layout.visibility = 'visible'


                self.qans_lbl.layout.visibility = 'hidden'
                self.qans_lbl.layout.display = 'none'

                self.writtenresp.layout.visibility = 'hidden'
                self.writtenresp.layout.display = 'none'

                self.display_only_answer.layout.visibility = 'hidden'
                self.display_only_answer.layout.display = 'none'


                chopts = []

                for choice in self.currentQuiz.getCurrentQuestion().getChoices():
                    chopts.append(choice[0])

                self.choices.options = [x for x in chopts]
                if autofill_answer is not None and autofill_answer != 'None':
                  self.choices.value = autofill_answer

            if self.currentQuiz.getCurrentQuestion().isProgrammingQuestion():
                self.qans_lbl.layout.display = 'block'
                self.qans_lbl.layout.visibility = 'visible'

                self.choices.layout.display = 'none'
                self.choices.layout.visibility = 'hidden'

                self.choices.layout.visibility = 'hidden'
                self.choices.layout.display = 'none'

                self.writtenresp.layout.visibility = 'hidden'
                self.writtenresp.layout.display = 'none'
                self.component_output.layout.visibility = 'hidden'
                self.component_output.layout.display = 'none'

                if autofill_answer is not None and autofill_answer != 'None':
                  self.display_only_answer.value = autofill_answer
                else:
                  self.display_only_answer.value = '<body><font color="green">Enter your answer in the cell below.</font></body>'

                self.display_only_answer.layout.visibility = 'visible'
                self.display_only_answer.layout.display = 'block'

            if self.currentQuiz.getCurrentQuestion().isOpenQuestion():
                if autofill_answer is not None and autofill_answer != 'None':
                    self.writtenresp.value = autofill_answer
                else:
                  self.writtenresp.value = ''

                self.qans_lbl.layout.display = 'block'
                self.qans_lbl.layout.visibility = 'visible'

                self.writtenresp.layout.display = 'block'
                self.writtenresp.layout.visibility = 'visible'

                self.choices.layout.visibility = 'hidden'
                self.choices.layout.display = 'none'

                self.display_only_answer.layout.visibility = 'hidden'
                self.display_only_answer.layout.display = 'none'

                self.component_output.layout.visibility = 'hidden'
                self.component_output.layout.display = 'none'

            if self.currentQuiz.getCurrentQuestion().isCustomQuestion():
                self.qans_lbl.layout.visibility = 'hidden'
                self.qans_lbl.layout.display = 'none'

                self.writtenresp.layout.visibility = 'hidden'
                self.writtenresp.layout.display = 'none'

                self.choices.layout.visibility = 'hidden'
                self.choices.layout.display = 'none'

                self.display_only_answer.layout.visibility = 'hidden'
                self.display_only_answer.layout.display = 'none'

                self.component_output.layout.display = 'block'
                self.component_output.layout.visibility = 'visible'

                question_name = self.currentQuiz.getCurrentQuestion().getTitle()
                component_name = self.currentQuiz.getCurrentQuestion().get_component_name()
                component_ui = self.get_component_ui(component_name, question_name)
                with self.component_output:
                    clear_output(wait=True)
                    display(component_ui)
                

            with self.feedback_out:
                clear_output(wait=True)

        except Exception as e:

            with self.feedback_out:
                clear_output(wait=True)
                print('open quest error .. '+str(e))

        return
    ##############################################################################################################

    def get_open_or_mchoice_answer_object(self,answer, question_type, correct):
      result_string = "correct" if correct else "incorrect"
      answer = {
          "type": question_type,
          "result": result_string,
          "answer": answer
      }
      return answer

    def check_selection(self,b):

        correct_answers = []

        if not self.currentQuiz is None:
            for choice in self.currentQuiz.getCurrentQuestion().getChoices():
                if self.currentQuiz.getCurrentQuestion().IsMChoice():
                    if choice[1]:
                        correct_answers.append(choice[0])
                else:
                    correct_answers = [choice[1]]
                    break

        question_title = self.currentQuiz.getCurrentQuestion().getTitle()

        if self.currentQuiz.getCurrentQuestion().IsMChoice():
            correct = False
            a = str(self.choices.value)
            if a in correct_answers:
                correct = True
                s = '\x1b[6;30;42m' + "Correct." + '\x1b[0m' +"\n" #green color
            else:
                s = '\x1b[5;30;41m' + "Incorrect. " + '\x1b[0m' +"\n" #red color
            answer_object = self.get_open_or_mchoice_answer_object(a, "multiple_choice", correct)
        elif self.currentQuiz.getCurrentQuestion().isProgrammingQuestion():
            feedback_lines, test_result, correct_keywords, total_keywords = ProgrammingQuestion.check_programming_question_answer(self.programmingQuestion, correct_answers[0]['tests'], correct_answers[0]['keywords'], correct_answers[0]['function_name'])
            s = feedback_lines
            answer_object = ProgrammingQuestion.get_programming_answer_object(self.programmingQuestion, test_result, correct_keywords, total_keywords)
        else:
            a = str(self.writtenresp.value)
            s = correct_answers[0]
            self.writtenresp.disabled = True
            answer_object = self.get_open_or_mchoice_answer_object(a, "open", True)

        with self.feedback_out:
            clear_output(wait=True)
            if not self.currentQuiz.getCurrentQuestion().IsMChoice():
                print('Correct Answer: ')
            else:
                s = 'Feedback: '+s

            print(s)

        #upload answer to drive
        self.drive.write_answer_to_file(answer_object, question_title + ".json")
        autofill_answer = self.get_autofill_answer(question_title)
        if autofill_answer is not None and autofill_answer != 'None':
          self.writtenresp.value = autofill_answer
          self.display_only_answer.value = autofill_answer

        self.drive.upload_log( question_title + ".json")
        return
    
    def submit_answer(self, answer):
        question = self.currentQuiz.getCurrentQuestion().getTitle()
        self.drive.write_answer_to_file(answer,question + '.json')
        self.drive.upload_log(question + '.json')
    

import io
import sys
import numpy as np
import re

class ProgrammingQuestion():
    def __init__(self, online_version):
        self.online_version = online_version

    def get_programming_answer_object(self,test_result, correct_keywords, total_keywords):

      answer = {
          "type": "programming",
          "result": test_result,
          "correct_keywords": correct_keywords,
          "total_keywords": total_keywords,
          "answer": self.get_programming_cell()
      }
      return answer
    
    def get_programming_cell(self):
      if self.online_version:
        from google.colab import _message
        notebook_json = _message.blocking_request('get_ipynb', request='', timeout_sec=5)
        code_lines = notebook_json["ipynb"]["cells"][1]["source"]
      else:
        import nbformat

        with open("quiz.ipynb") as f:
            nb = nbformat.read(f, as_version=4)

        code_cel = nb.cells[1]
        if code_cel.cell_type == 'code':
            code_lines = code_cel.source.splitlines(keepends=True)
        else:
            code_lines = []

      return code_lines
    
    def get_correct_tests(self, results):
      return sum(1 for v in results.values() if v['correct'])
    
    def test_programming_function(self,compiled_function, tests, function_name):
      result = {}

      namespace = {}
      exec(compiled_function, namespace)
      count = 0
      for parameters, expected in tests.items():
        func = namespace[function_name]
        try:
        
          params = eval(parameters, namespace)

          if isinstance(params, tuple):
              answer = func(*params)
          elif parameters == "":
              answer = func()
          else:
              answer = func(params)
              
          try:
              if isinstance(answer, np.ndarray):
                  answer = answer.tolist()
          except:
              pass
          result[parameters] = {
              'result': answer,
              'expected': expected,
              'correct': str(answer).strip() == str(expected).strip()
          }
        except Exception as e:
            s = str(e)
            print("error: " + s)
      return result

    def test_programming_function_without_return(self, compiled_code, tests, function_name):
        result = {}
        namespace = {}
        exec(compiled_code, namespace)

        func = namespace[function_name]
        for parameters, expected in tests.items():

            old_stdout = sys.stdout
            sys.stdout = captured_output = io.StringIO()
            try:
                params = eval(parameters, namespace) if parameters else ()
                if isinstance(params, tuple):
                  func(*params)
                elif parameters == "":
                  func()
                else:
                  func(params)
            except Exception as e:
                captured_output.write(f"Error: {e}")
            finally:
                sys.stdout = old_stdout

            printed_output = captured_output.getvalue().strip()
            
            if isinstance(expected, list):
                correct = all(exp in printed_output for exp in expected)
            else:
                expected = expected.strip()
                correct = expected in printed_output

            result[parameters] = {
                'result': printed_output,
                'expected': expected,
                'correct': correct
            }

        return result
    
    def get_formatted_feedback(self, test_result, correct_keywords, total_keywords):
      correct_tests = self.get_correct_tests(test_result)
      total_tests = len(test_result)

      total = total_tests + total_keywords
      total_correct = correct_tests + correct_keywords

      feedback_lines = [f"Tests passed: {total_correct} out of {total}"]

      # for inp, res in test_result.items():
      #     feedback_lines.append(f"Input: {inp}")
      #     feedback_lines.append(f"Expected Output: {res['expected']}")
      #     feedback_lines.append(f"Received Output: {res['result']}")
      #     feedback_lines.append(f"Correct: {res['correct']}")
      #     feedback_lines.append("-----------------")

      return "\n".join(feedback_lines)

    def get_correct_keywords(self,keywords, code_str):
      count = 0
      for word in keywords:
        if str(word).strip().replace(" ", "") in str(code_str).strip().replace(" ", ""):
          count += 1
      return count
    
    def check_programming_question_answer(self,tests,keywords,function_name):
      code_lines = self.get_programming_cell()
      code_str = ''.join(code_lines)
      correct_keywords = self.get_correct_keywords(keywords, code_str)
      total_keywords = len(keywords)
      try:
        if "def" not in code_str or "class" in code_str:
          code_lines = code_str.splitlines()
          indented_code = ["    " + line for line in code_lines]
          code_str = "def default_function():\n" + "\n".join(indented_code)
        compiled_code = compile (code_str, 'test', 'exec')
      except:
        return 'Compile error, check your answer in the below cell', None, correct_keywords, total_keywords
      
      if 'return' in code_str and "class" not in code_str:
        if function_name in code_str:
          test_result = self.test_programming_function(compiled_code, tests, function_name)
        else:
           pattern = r'^\s*def\s+([a-zA-Z_]\w*)\s*\('
           matches = re.findall(pattern, code_str, re.MULTILINE)
           if len(matches) == 1:
              test_result = self.test_programming_function(compiled_code, tests, matches[0])
           else:
              test_result = {}       
              test_result[''] = {
                'result': 'Error: no/multiple functions implemented',
                'expected': '',
                'correct': False
            }
      else:
         test_result  = self.test_programming_function_without_return(compiled_code, tests, function_name)
      feedback_lines = self.get_formatted_feedback(test_result, correct_keywords, total_keywords)

      return feedback_lines, test_result, correct_keywords, total_keywords
    
    

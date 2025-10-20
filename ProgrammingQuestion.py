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
            answer = eval(f"{function_name}({parameters})", namespace)
            result[parameters] = {
                'result': answer,
                'expected': expected,
                'correct': answer == expected
            }
        except Exception as e:
            s = str(e)
            print("error: " + s)
      return result
    
    def get_formatted_feedback(self, test_result, correct_keywords, total_keywords):
      correct_tests = self.get_correct_tests(test_result)
      total_tests = len(test_result)

      feedback_lines = [f"Tests passed: {correct_tests} out of {total_tests}",
                        f"Keywords: {correct_keywords} out of {total_keywords}",
                        "-----------------------------------------------------------"]

      for inp, res in test_result.items():
          feedback_lines.append(f"Input: {inp}")
          feedback_lines.append(f"Expected Output: {res['expected']}")
          feedback_lines.append(f"Received Output: {res['result']}")
          feedback_lines.append(f"Correct: {res['correct']}")
          feedback_lines.append("-----------------")

      return "\n".join(feedback_lines)

    def get_correct_keywords(self,keywords, code_str):
      count = 0
      for word in keywords:
        if word in  code_str:
          count += 1
      return count
    
    def check_programming_question_answer(self,tests,keywords,function_name):
      code_lines = self.get_programming_cell()
      code_str = ''.join(code_lines)
      correct_keywords = self.get_correct_keywords(keywords, code_str)
      total_keywords = len(keywords)

      try:
        compiled_code = compile (code_str, 'test', 'exec')
      except:
        return 'Compile error, check your answer in the below cell', None, correct_keywords, total_keywords

      test_result = self.test_programming_function(compiled_code, tests, function_name)
      feedback_lines = self.get_formatted_feedback(test_result, correct_keywords, total_keywords)

      return feedback_lines, test_result, correct_keywords, total_keywords
    
    

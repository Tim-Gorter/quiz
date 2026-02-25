class QuestionsList:
    def __init__(self):
        self.questions = [
        #     {
        #     "title": "Question 1",
        #     "text": "Noem een voordeel en een nadeel van het feit dat Python dynamisch getypeerd is",
        #     "component": "quiz",
        #     "choices": "",
        #     "type":"open",
        #     "correctness":"Een voordeel is: type casting is niet nodig. Een nadeel is: fouten met betrekking tot typen worden er niet door een compiler uitgehaald; je komt ze pas tegen tijdens het draaien van een programma."
        # },{
        #     "title": "Question 2",
        #     "text": "Bij elke waarde hoort één type? Welke van de uitspraken over deze stelling is juist?",
        #     "component": "quiz",
        #     "choices": ["De uitspraak geldt alleen voor dynamische typering.", "De uitspraak geldt alleen voor statische typering.", "De uitspraak geldt voor zowel statische als dynamische typering.", "De uitspraak heeft tot gevolg dat elke variabele een vast type heeft.","De uitspraak heeft niet tot gevolg dat elke variabele een vast type heeft."],
        #     "type":"multiple_choice",
        #     "correctness":[False,False,True,False,False]
        # }
        # ,{
        #     "title": "Question 3",
        #     "text": "Implementeer een functie square() die één parameter accepteert en het kwadraat van dat getal teruggeeft",
        #     "component": "quiz",
        #     "choices": "",
        #     "type":"programming",
        #     "correctness":{
        #         "tests": {"2":4,"3":9,"4":16},
        #         "keywords": ["for", "in", "print"],
        #         "function_name": "square"
        #         }
        # }, {
        # "title": "LAB-Question1",
        # "text": "A dietician claims that adults in a country consume an average of 1500 calories per day. A researcher believes that the average calorie consumption is higher. They collected data from a random sample of 30 adults and find that the sample mean is 1600 calories, with a sample standard deviation of 150 calories. At a significance level of 0.05, can the researcher conclude that the average calorie consumption is higher than 1500 calories?",
        # "choices": "",
        # "component": "Statistics",
        # "parameters": [] ,
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "LAB-Question2",
        # "text": "A manufacturer of a new type of battery claims that their batteries last an average of 40 hours under continuous use. A consumer testing agency wants to investigate this claim. They randomly select 20 batteries and find that the sample mean lifespan is 38.5 hours, with a sample standard deviation of 3 hours. At a significance level of 0.02, can the agency conclude that the manufacturer's claim is false?",
        # "choices": "",
        # "component": "Statistics",
        # "parameters": [] ,
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "LAB-Question3",
        # "text": "A political campaign claims that at least 55% of voters in a certain city support their candidate.   A random sample of 300 voters was taken, and it was found that 150 voters supported the candidate. At the 5% significance level, test whether there is enough evidence to reject the campaign's claim.",
        # "choices": "",
        # "component": "Statistics",
        # "parameters": [] ,
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "LAB-Question4",
        # "text": "A national health organization claims that 65% of adults in a certain country get the recommended amount of daily exercise. A local health department believes this percentage is lower in their region. They conduct a random survey of 250 adults in their region and find that 150 of them meet the recommended exercise guidelines. At a significance level of 0.05, can the local health department conclude that the national organization's claim is false for their region?",
        # "choices": "",
        # "component": "Statistics",
        # "parameters": [] ,
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "LAB-Question5",
        # "text": "The Acme Company has developed a new battery. The engineer in charge claims that the new battery will operate continuously for at least 7 minutes longer than the old battery.To test the claim, the company selects a simple random sample of 100 new batteries and 100 old batteries. The old batteries run continuously for 200 minutes with a standard deviation of 20 minutes; the new batteries, 200 minutes with a standard deviation of 40 minutes. Test the engineer's claim that the new batteries run at least 7 minutes longer than the old. Use a 0.05 level of significance. (Assume that there are no outliers in either sample.)",
        # "choices": "",
        # "component": "Statistics",
        # "parameters": [] ,
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "LAB-Question6",
        # "text": "The local baseball team conducts a study to find the amount spent on refreshments at the ball park. Over the course of the season they gather simple random samples of 100 men and 100 women. For men, the average expenditure was $200, with a standard deviation of $40. For women, it was $190, with a standard deviation of $20. The team owner claims that men spend at least $7 more than women. Assume that the two populations are independent and normally distributed.",
        # "choices": "",
        # "component": "Statistics",
        # "parameters": [] ,
        # "type":"custom",
        # "correctness":{}
        # },{
        #     "title": "IB3502 - 1.1",
        #     "text": "Part 1.1.A. Dataset Description. Describe the data set by specifying its main properties like the number of features and its size. Discuss the main goal of the described analysis with the data by elaborating the existence and the type of its label. Which features can be dropped do you think as they do not carry valuable informaton for a predictive analysis and why? (5 pts) ",
        #     "choices": "",
        #     "type":"programming",
        #     "correctness":{
        #         "tests": {},
        #         "keywords": [],
        #         "function_name": ""
        #         }
        # }, 
        # {
        # "title": "Data visualisation 1",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "1.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 2",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "2.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 3",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["Temperature", "Date"], "3.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 4",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["Temperature", "Date"], "4.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 5",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "5.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 6",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "6.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 7",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "7.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 8",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "8.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 9",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "9.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 10",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "10.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 11",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "11.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 12",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "12.png"], 
        # "type":"custom",
        # "correctness":{}
        # }, {
        # "title": "Data visualisation 13",
        # "text": "Which properties apply to the given visualisation?.",
        # "choices": "",
        # "component": "DataVisualisation",
        # "parameters":[["MPG", "Acceleration"], "12.png"], 
        # "type":"custom",
        # "correctness":{}
        # } ,
        {
            "title": "Lab exercises part 1",
            "text":"Part 1. Basic Python (20-30 minutes)",
            "component": "Python lab exercises",
            "choices": "",
            "type":"info",
            "correctness":{}
        },
        {
            "title": "1. Question 1",
            "text": "Write a function \"repeat_message\" that takes two inputs: a message (string) and a number (integer). The function should print the message the specified number of times.",
            "component": "Python lab exercises",
            "choices": "",
            "type":"programming",
            "correctness":{
                "tests": [
                            {
                                "name": "Repeats message 3 times",
                                "type": "return",
                                "input": "('Hello', 3)",
                                "expected": "Hello\nHello\nHello\n"
                            },
                            {
                                "name": "Repeats message once",
                                "type": "return",
                                "input": "('Test', 1)",
                                "expected": "Test\n"
                            },
                            {
                                "name": "Zero repetitions prints nothing",
                                "type": "return",
                                "input": "('nothing', 0)",
                                "expected": ""
                            }
                        ],
                "keywords": ["for", "in", "print"],
                "function_name": "repeat_message"
                }
        },{
            "title": "1. Question 2",
            "text": "Write a function \"calculate_average\" that takes a list of numbers as input and returns the average (mean) of those numbers.",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Average of five numbers",
                        "type": "return",
                        "input": "([1, 2, 3, 4, 5])",
                        "expected": 3.0
                    },
                    {
                        "name": "Average of three numbers",
                        "type": "return",
                        "input": "([10, 20, 30])",
                        "expected": 20.0
                    },
                    {
                        "name": "Average of single number",
                        "type": "return",
                        "input": "([7])",
                        "expected": 7.0
                    }
                ],
                "keywords": ["for", "in"],
                "function_name": "calculate_average"
            }
        }
        ,{
            "title": "1. Question 3",
            "text": "Write a program (using a loop!) that counts and prints the number of occurences of the word \"cat\" in the list [\"duck\", \"chicken\", \"mouse\", \"dog\", \"fox\", \"car\", \"cat\" ,\"cat\" ] ",
            "component": "Python lab exercises",
            "choices": "",
            "type":"programming",
            "correctness":{
            "tests": [
                {
                    "name": "Counts occurrences of 'cat'",
                    "type": "output",
                    "input": "",
                    "expected": "2\n"
                }
            ],
            "keywords": ["for", "in", "print"],
            "function_name": "default_function"
            }
        },{
            "title": "1. Question 4",
            "text": "Create a function called \"countletter\" that uses linear search to return how often a given character is in a given string. For example, count the number of \"l\" in the phrase \"Hello, world!\" ",
            "component": "Python lab exercises",
            "choices": "",
            "type":"programming",
            "correctness":{
                "tests": [
                    {
                        "name": "Counts letter occurrences",
                        "type": "return",
                        "input": "('Hello world !', 'l')",
                        "expected": 3
                    }
                ],
                "keywords": ["for", "in"],
                "function_name": "countletter"
                }
        },{
            "title": "1. Question 5",
            "text": "Write a program which prints all numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 2080 (both included).",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Print numbers divisible by 7 and not multiple of 5",
                        "type": "output",
                        "input": "",
                        "expected": [2002, 2009, 2016, 2023, 2037, 2044]
                    }
                ],
                "keywords": ["for", "in"],
                "function_name": "default_function"
            }
        },
        {
            "title": "1. Question 6",
            "text": "Use list comprehension for the question 5",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "List comprehension result",
                        "type": "return",
                        "input": "",
                        "expected": [2002, 2009, 2016, 2023, 2037, 2044]
                    }
                ],
                "keywords": ["for", "in", "[", "]"],
                "function_name": "default_function"
            }
        },
        {
            "title": "1. Question 7",
            "text": "Use map and lambda functions for the question 6. ",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Map and lambda result",
                        "type": "return",
                        "input": "",
                        "expected": [2002, 2009, 2016, 2023, 2037, 2044]
                    }
                ],
                "keywords": ["lambda", "filter"],
                "function_name": "default_function"
            }
        },
                {
            "title": "1. Question 8",
            "text": "Write a function \"count_strings\" that takes a list of strings as input and returns the number of strings where the string length is 2 or more and the first and last characters are the same. Go to the editor Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2 ",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Counts valid strings (example 1)",
                        "type": "return",
                        "input": "(['abc', 'xyz', 'aba', '1221'])",
                        "expected": 2
                    },
                    {
                        "name": "Counts valid strings (example 2)",
                        "type": "return",
                        "input": "(['abc', 'xyz', 'aba', '1221', 'jooj', 'legermeetsysteelregel', 'madam', 'ikke', 'gij', 'fietser'])",
                        "expected": 5
                    }
                ],
                "keywords": [],
                "function_name": "count_strings"
            }
        },{
            "title": "1. Question 9",
            "text": "Write a function \"modify_list\" that takes a list of numbers as input and modifies it by reference such that the elements at positions 3, 5, and 6 are set to the value of the element in the next position.",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Modifies list by reference",
                        "type": "return",
                        "input": "([0,1,2,3,4,5,6,7,8])",
                        "expected": [0, 1, 2, 4, 4, 6, 6, 7, 7, 8]
                    }
                ],
                "keywords": ["assert"],
                "function_name": "modify_list"
            }
        },{
            "title": "1. Question 10",
            "text": "All Dice Combinations. Write a list comprehension that uses nested for-clauses to create a single list with all 36 different dice combinations from (1,1) to (6,6).",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                {
                    "name": "All dice combinations",
                    "type": "return",
                    "input": "",
                    "expected": "[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]",
                },
                ],
                "keywords": [""],
                "function_name": "default_function"
            }
        },        {
            "title": "Lab exercises part 2",
            "text":"Part 2. Object Orientation and Inheritence (20-30 minutes)",
            "component": "Python lab exercises",
            "choices": "",
            "type":"info",
            "correctness":{}
        },{
            "title": "2. Question 1",
            "text": "Implement a program that simulates the bouncing of a basketball, football, and tennis ball from an initial height of 100 meters. \nEach ball has a specific bounce ratio (0.8, 0.6, and 0.5 respectively).\nThe program should calculate and print the total distance each ball travels in the air until its bounce height falls below 1 meter.\nExplain how the Bounce() function calculates the distance traveled during each bounce, and how the while loop determines when to stop the simulation.\nCreate a Ball class as a superclass. Basketball, Football, and Tennisball are the subclasses that should inherit the superclass.",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Basketball total distance",
                        "type": "class_method",
                        "class_name": "Basketball",
                        "input": "100",
                        "method": "bounce",
                        "expected": 890
                    },
                    {
                        "name": "Football total distance",
                        "type": "class_method",
                        "class_name": "Football",
                        "input": "100",
                        "method": "bounce",
                        "expected": 396
                    },
                    {
                        "name": "Tennisball total distance",
                        "type": "class_method",
                        "class_name": "Tennisball",
                        "input": "100",
                        "method": "bounce",
                        "expected": 296
                    },
                    {
                        "name": "Basketball inherits Ball",
                        "type": "inheritance",
                        "class_name": "Basketball",
                        "parent_class": "Ball"
                    },
                    {
                        "name": "Football inherits Ball",
                        "type": "inheritance",
                        "class_name": "Football",
                        "parent_class": "Ball"
                    },
                    {
                        "name": "Tennisball inherits Ball",
                        "type": "inheritance",
                        "class_name": "Tennisball",
                        "parent_class": "Ball"
                    }
                ],
                "keywords": ["class"],
                "function_name": "default_function"
            }
        },        {
            "title": "Lab exercises part 3",
            "text":"Part 3. Numpy (30 minutes)",
            "component": "Python lab exercises",
            "choices": "",
            "type":"info",
            "correctness":{}
        },{
            "title": "3. Question 1",
            "text": "Import the numpy package under the name np",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [],
                "keywords": ["import numpy as np"],
                "function_name": "default_function"
            }
        },
        {
            "title": "3. Question 2",
            "text": "Create a null vector of size 10",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [],
                "keywords": ["np.zeros(10)"],
                "function_name": "default_function"
            }
        },
        {
            "title": "3. Question 3",
            "text": "Create a null vector of size 10 but the fifth value which is 1",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [],
                "keywords": ["np.zeros(10)","[4]"],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 4",
            "text": "Create a vector with values ranging from 10 to 49",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [],
                "keywords": ["np.arange(10,49)"],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 5",
            "text": "Find indices of non-zero elements from np.array([1,2,0,0,4,0])",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Non-zero indices",
                        "type": "output",
                        "input": "",
                        "expected": "0\n1\n4\n"
                    }
                ],
                "keywords": ["[1,2,0,0,4,0]",],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 6",
            "text": "Create a 10x10 array with random values and find the minimum and maximum values",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [],
                "keywords": ["randn(10,10)","np.max","np.min"],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 7",
            "text": "Create a random vector of size 30 and find the mean value",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [],
                "keywords": ["random.randn(30)","mean("],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 8",
            "text": "Create a random vector of size 30 and find the mean value",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests":[],
                "keywords": ["random.randn(10)","sort("],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 9",
            "text": "Create random vector of size 10 and replace the maximum value by 0",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": []
                ,
                "keywords": ["random.randn(10)","]=0",],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 10",
            "text": "Consider two random array A and B, check if they are equal",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": []
                ,
                "keywords": ["random.randn"],
                "function_name": "default_function"
            }
        }
        ,{
            "title": "3. Question 11",
            "text": "Given the following function:\ndef maxx(x, y):\n    \"\"\"Get the maximum of two items\"\"\"\n    if x >= y:\n        return x\n    else:\n        return y\nmaxx(1, 5)\n\nUse vectorization to apply it to vectors:\n[1,4,5,6,9] and [9,3,3,9,11]",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": []
                ,
                "keywords": ["vectorize(maxx)","[1,4,5,6,9]","[9,3,3,9,11]"],
                "function_name": "default_function"
            }
        },{
            "title": "3. Question 12",
            "text": "Check numpy boolean indexing. Get the positions where elements of a and b match: \na = np.array([1,2,3,2,3,4,3,4,5,6])\nb = np.array([7,2,10,2,7,4,9,4,9,8])",
            "component": "Python lab exercises",
            "choices": "",
            "type": "programming",
            "correctness": {
                "tests": [
                    {
                        "name": "Matching positions",
                        "type": "output",
                        "input": "",
                        "expected": "1\n3\n5\n7\n"
                    }
                ],
                "keywords": ["where(a==b)"],
                "function_name": "default_function"
            }
        },{
                "title": "3. Question 13",
                "text": "Write a function \"find_nearest_value\" that takes a list of numbers and a target value as input and returns the number from the list that is closest to the target value.\n\nexample the array: [1,2,4,8,9,10] and the value: 5",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                    {
                        "name": "Nearest value test 1",
                        "type": "return",
                        "input": "([1, 2, 4, 8, 9, 10], 5)",
                        "expected": 4
                    },
                    {
                        "name": "Nearest value test 2",
                        "type": "return",
                        "input": "([1, 3, 7, 8], 6)",
                        "expected": 7
                    },
                    {
                        "name": "Nearest value test 3",
                        "type": "return",
                        "input": "([2, 5, 6, 12], 10)",
                        "expected": 12
                    },
                    {
                        "name": "Nearest value test 4",
                        "type": "return",
                        "input": "([0, 20, 50], 18)",
                        "expected": 20
                    }
                ],
                    "keywords": [],
                    "function_name": "find_nearest_value"
                }
            },{
                "title": "3. Question 14",
                "text": "Write a function \"moving_average\" that takes a list of numbers and a window size n as input and returns a list containing the moving averages computed over a sliding window of size n.\n\nExample array: [0.4459046, -0.10303952, 0.93106738, 1.40359842]\nWindow size: 3\nOutput: [0.42464415, 0.74387543]\n\nhint: np.cumsum can help you here.",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Moving average example",
                            "type": "return",
                            "input": "([0.4459046, -0.10303952, 0.93106738, 1.40359842], 3)",
                            "expected": [0.42464415333333333, 0.7438754266666666]
                        },
                        {
                            "name": "Moving average test 2",
                            "type": "return",
                            "input": "([1, 2, 3, 4, 5], 2)",
                            "expected": [1.5, 2.5, 3.5, 4.5]
                        },
                        {
                            "name": "Moving average test 3",
                            "type": "return",
                            "input": "([10, 20, 30, 40], 3)",
                            "expected": [20.0, 30.0]
                        },
                        {
                            "name": "Moving average test 4",
                            "type": "return",
                            "input": "([5, 5, 5, 5], 4)",
                            "expected": [5.0]
                        }
                    ],
                    "keywords": [],
                    "function_name": "moving_average"
                }
            },       {
                "title": "Lab exercises part 4",
                "text":"Part 4. Pandas (30 minutes) \n\nThe following code imports numpy and pandas. It imports the data from the url https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv. The it assigns it to a variable called chipo.\n\nimport pandas as pd\nurl = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'\nchipo = pd.read_csv(url, sep = '\\t')\nchipo",
                "component": "Python lab exercises",
                "choices": "",
                "type":"info",
                "correctness":{}
            },{
                "title": "4. Question 1",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint the first 10 entries",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Print first 10 entries",
                            "type": "output",
                            "input": "",
                            "expected": [
                                "Chips and Fresh Tomato Salsa",
                                "Izze",
                                "Nantucket Nectar",
                                "Chips and Tomatillo-Green Chili Salsa",
                                "Chicken Bowl",
                                "Side of Chips",
                                "Steak Burrito",
                                "Steak Soft Tacos",
                                "$2.39",
                                "$3.39",
                                "[Clementine]",
                                "[Apple]"
                                ]
                        }
                    ],
                    "keywords": [".head(10)"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 2",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint the number of observations in the dataset",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Number of observations",
                            "type": "output",
                            "input": "",
                            "expected": "4622"
                        }
                    ],
                    "keywords": [".shape[0]"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 3",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint the number of columns in the dataset",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Number of columns",
                            "type": "output",
                            "input": "",
                            "expected": "5"
                        }
                    ],
                    "keywords": [".shape[1]"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 4",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint the name of all the columns.",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Column names",
                            "type": "output",
                            "input": "",
                            "expected": ["order_id", "quantity", "item_name", "choice_description", "item_price"],
                        }
                    ],
                    "keywords": ["columns.tolist()"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 5",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nHow is the dataset indexed? Print the index",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Print index",
                            "type": "output",
                            "input": "",
                            "expected": ["RangeIndex(start=0, stop=4622, step=1)"],
                        }
                    ],
                    "keywords": [".index"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 6",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint the most ordered item",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Most ordered item",
                            "type": "output",
                            "input": "",
                            "expected": "Chicken Bowl"
                        }
                    ],
                    "keywords": [".value_counts()"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 7",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint how many items were ordered",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Number of most ordered items",
                            "type": "output",
                            "input": "",
                            "expected": "726"
                        }
                    ],
                    "keywords": ["iloc[0]"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 8",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint the most ordered item in the choice_description column",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Most ordered choice description",
                            "type": "output",
                            "input": "",
                            "expected": "Diet Coke"
                        }
                    ],
                    "keywords": ["value_counts()", "index[0]"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 9",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint how many items were ordered in total",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Total number of items ordered",
                            "type": "output",
                            "input": "",
                        "expected": ["4972"],
                        }
                    ],
                    "keywords": ["sum"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 10",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nTurn the item price into a float",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [],
                    "keywords": ["replace", "astype(float)"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 11",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint how much the revenue was for the period in the dataset",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Total revenue",
                            "type": "output",
                            "input": "",
                            "expected": ["39237"],
                        }
                    ],
                    "keywords": ["sum", "quantity", "item_price"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 12",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint how many orders were made in the period?",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Number of orders",
                            "type": "output",
                            "input": "",
                            "expected": ["1834"],
                        }
                    ],
                    "keywords": ["nunique"],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 13",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint the average amount per order?",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Average amount per order",
                            "type": "output",
                            "input": "",
                            "expected": ["21"],
                        }
                    ],
                    "keywords": [],
                    "function_name": "default_function"
                }
            },{
                "title": "4. Question 14",
                "text": "Implement the following steps for the dataframe called \"chipo\" (see Lab exercises part 4):\nPrint how many different items are sold?",
                "component": "Python lab exercises",
                "choices": "",
                "type": "programming",
                "correctness": {
                    "tests": [
                        {
                            "name": "Number of different items",
                            "type": "output",
                            "input": "",
                            "expected": ["50"],
                        }
                    ],
                    "keywords": ["nunique"],
                    "function_name": "default_function"
                }
            }
        ]
        
    def get_questions(self):
        return self.questions
    
    def get_questions_master_version(self):
        return [q for q in self.questions if q.get("type") != "info"]
    
    def get_components(self):
        components = {q.get("component") for q in self.questions if "component" in q}
        return list(components)
    
    def get_filtered_questions(self, component):
        return [q for q in self.questions if q.get("component") == component]
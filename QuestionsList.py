class QuestionsList:
    def __init__(self):
        self.questions = [
            {
            "title": "Question 1",
            "text": "Noem een voordeel en een nadeel van het feit dat Python dynamisch getypeerd is",
            "component": "quiz",
            "choices": "",
            "type":"open",
            "correctness":"Een voordeel is: type casting is niet nodig. Een nadeel is: fouten met betrekking tot typen worden er niet door een compiler uitgehaald; je komt ze pas tegen tijdens het draaien van een programma."
        },{
            "title": "Question 2",
            "text": "Bij elke waarde hoort één type? Welke van de uitspraken over deze stelling is juist?",
            "component": "quiz",
            "choices": ["De uitspraak geldt alleen voor dynamische typering.", "De uitspraak geldt alleen voor statische typering.", "De uitspraak geldt voor zowel statische als dynamische typering.", "De uitspraak heeft tot gevolg dat elke variabele een vast type heeft.","De uitspraak heeft niet tot gevolg dat elke variabele een vast type heeft."],
            "type":"multiple_choice",
            "correctness":[False,False,True,False,False]
        }
        ,{
            "title": "Question 3",
            "text": "Implementeer een functie square() die één parameter accepteert en het kwadraat van dat getal teruggeeft",
            "component": "quiz",
            "choices": "",
            "type":"programming",
            "correctness":{
                "tests": {"2":4,"3":9,"4":16},
                "keywords": ["for", "in", "print"],
                "function_name": "square"
                }
        }, {
        "title": "LAB-Question1",
        "text": "A dietician claims that adults in a country consume an average of 1500 calories per day. A researcher believes that the average calorie consumption is higher. They collected data from a random sample of 30 adults and find that the sample mean is 1600 calories, with a sample standard deviation of 150 calories. At a significance level of 0.05, can the researcher conclude that the average calorie consumption is higher than 1500 calories?",
        "choices": "",
        "component": "Statistics",
        "parameters": [] ,
        "type":"custom",
        "correctness":{}
        }, {
        "title": "LAB-Question2",
        "text": "A manufacturer of a new type of battery claims that their batteries last an average of 40 hours under continuous use. A consumer testing agency wants to investigate this claim. They randomly select 20 batteries and find that the sample mean lifespan is 38.5 hours, with a sample standard deviation of 3 hours. At a significance level of 0.02, can the agency conclude that the manufacturer's claim is false?",
        "choices": "",
        "component": "Statistics",
        "parameters": [] ,
        "type":"custom",
        "correctness":{}
        }, {
        "title": "LAB-Question3",
        "text": "A political campaign claims that at least 55% of voters in a certain city support their candidate.   A random sample of 300 voters was taken, and it was found that 150 voters supported the candidate. At the 5% significance level, test whether there is enough evidence to reject the campaign's claim.",
        "choices": "",
        "component": "Statistics",
        "parameters": [] ,
        "type":"custom",
        "correctness":{}
        }, {
        "title": "LAB-Question4",
        "text": "A national health organization claims that 65% of adults in a certain country get the recommended amount of daily exercise. A local health department believes this percentage is lower in their region. They conduct a random survey of 250 adults in their region and find that 150 of them meet the recommended exercise guidelines. At a significance level of 0.05, can the local health department conclude that the national organization's claim is false for their region?",
        "choices": "",
        "component": "Statistics",
        "parameters": [] ,
        "type":"custom",
        "correctness":{}
        }, {
        "title": "LAB-Question5",
        "text": "The Acme Company has developed a new battery. The engineer in charge claims that the new battery will operate continuously for at least 7 minutes longer than the old battery.To test the claim, the company selects a simple random sample of 100 new batteries and 100 old batteries. The old batteries run continuously for 200 minutes with a standard deviation of 20 minutes; the new batteries, 200 minutes with a standard deviation of 40 minutes. Test the engineer's claim that the new batteries run at least 7 minutes longer than the old. Use a 0.05 level of significance. (Assume that there are no outliers in either sample.)",
        "choices": "",
        "component": "Statistics",
        "parameters": [] ,
        "type":"custom",
        "correctness":{}
        }, {
        "title": "LAB-Question6",
        "text": "The local baseball team conducts a study to find the amount spent on refreshments at the ball park. Over the course of the season they gather simple random samples of 100 men and 100 women. For men, the average expenditure was $200, with a standard deviation of $40. For women, it was $190, with a standard deviation of $20. The team owner claims that men spend at least $7 more than women. Assume that the two populations are independent and normally distributed.",
        "choices": "",
        "component": "Statistics",
        "parameters": [] ,
        "type":"custom",
        "correctness":{}
        },{
            "title": "IB3502 - 1.1",
            "text": "Part 1.1.A. Dataset Description. Describe the data set by specifying its main properties like the number of features and its size. Discuss the main goal of the described analysis with the data by elaborating the existence and the type of its label. Which features can be dropped do you think as they do not carry valuable informaton for a predictive analysis and why? (5 pts) ",
            "choices": "",
            "type":"programming",
            "correctness":{
                "tests": {},
                "keywords": [],
                "function_name": ""
                }
        }, 
        {
        "title": "Data visualisation 1",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "1.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 2",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "2.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 3",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "3.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 4",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "4.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 5",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "5.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 6",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "6.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 7",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "7.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 8",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "8.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 9",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "9.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 10",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "10.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 11",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "11.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 12",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "12.png"], 
        "type":"custom",
        "correctness":{}
        }, {
        "title": "Data visualisation 13",
        "text": "Which properties apply to the given visualisation?.",
        "choices": "",
        "component": "DataVisualisation",
        "parameters":[["MPG", "Acceleration"], "12.png"], 
        "type":"custom",
        "correctness":{}
        }
        ]
        
    def get_questions(self):
        return self.questions
    
    def get_components(self):
        components = {q.get("component") for q in self.questions if "component" in q}
        return list(components)
    
    def get_filtered_questions(self, component):
        return [q for q in self.questions if q.get("component") == component]
questions = [
    {
        "question": "The ability of one class to acquire methods and attributes from another class is called:",
        "options": {
            "A": " Inheritance",
            "B": " Abstraction",
            "C": " Polymorphism",
            "D": " Object"
        }
    },
    {
        "question": "Which OOP concept refers to wrapping data and methods into a single unit?",
        "options": {
            "A": " Inheritance",
            "B": "Encapsulation",
            "C": " Abstraction",
            "D": " Polymorphism"
        },
    },
    {
        "question": "Which keyword is used to define a class in Python?",
        "options": {
            "A": " define",
            "B": " class",
            "C": " structure",
            "D": " object"
        }
    },
    {
        "question": "A function defined inside a class is called a:",
        "options": {
            "A": " Method",
            "B": " Attribute",
            "C": " Module",
            "D": " Function"
        }

    },
    {
        "question": "Which OOP feature allows the same method name to have different implementations?",
        "options": {
            "A": " Inheritance",
            "B": " Encapsulation",
            "C": " Abstraction",
            "D": " Polymorphism"
        }
    }
]
answers = [
    {
        "q1": "The ability of one class to acquire methods and attributes from another class is called:",
        "A": "Inheritance"
    },
    {
        "q2": "Which OOP concept refers to wrapping data and methods into a single unit?",
        "B": "Encapsulation"
    },
    {
        "q3": "Which keyword is used to define a class in Python?",
        "B": " class"
    },
    {
        "q4": "A function defined inside a class is called a:",
        "A": " Method"
    },
    {
        "q5": "Which OOP feature allows the same method name to have different implementations?",
        "D": " Polymorphism"
    }
]
score = 0
for q_no, ques in enumerate(questions):
    print(q_no+1, questions[q_no]["question"])
    for option, answer in ques["options"].items():
        print(option, answer)
    print()
    guess = input("enter your answer: ").upper()
    if guess == list(answers[q_no].keys())[1]:
        score += 1
print(f"Your score: {score}")

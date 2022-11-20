#dictionary that stores questions and answers
#variable that tracks the score of the player
#loop through the dictionary using key value pairs
#display each questions to the user and allow them to answer
#tell them if they are right or wrong
#show the final result when quiz is completed

quiz= {
    "question1":{
        "question":"What is the currency of Portugal?",
        "answer":"Euro"
    }, 
    "question2":{
        "question": "A marathon is how many miles?....(Enter in number)",
        "answer":"26"
    },  
    "question3":{
        "question":"What does www stand for in the context of an internet address?",
        "answer": "World wide web"
    },
    "question4":{
        "question":"Which of these precious metals is more expensive per ounce, gold or silver?",
        "answer":"Gold"
    },
    "question5":{
        "question":"Which is bigger, A4 paper or A5 paper?",
        "answer":"A4"
    },
    "question6":{
        "question":"H20 is the chemical formula for what?",
        "answer":"Water"
    },
    "question7":{
        "question":"Which gas is used to fill balloons?",
        "answer":"Helium"
    },
    "question8":{
        "question":"What is the number 5 in roman numerals?",
        "answer":"V"
    },
    "question9":{
        "question":"What is the yellowish orange part of an egg called?",
        "answer":"Yolk"
    },
    "question10":{
        "question":"How many legs do insects have?....(Enter in number)",
        "answer":"6"
    }, 
    "question11":{
        "question":"What is a baby kangaroo called??",
        "answer":"Joey"
    },
    "question12":{
        "question":"What is the closest planet to the Sun?",
        "answer":"Mercury"
    },
    "question13":{
        "question":"In which country can you find the Eiffel Tower",
        "answer":"France"
    },
    "question14":{
        "question":"How many days are there in a leap year?...",
        "answer":"366"
    },
    "question15":{
        "question":"How many players are in a soccer team?....(Enter in number)",
        "answer":"11"
    },
    "question16":{
        "question":"Where do polar bears live?",
        "answer":"The arctic ocean"
    },
    "question17":{
        "question":"Which is faster, light or sound?",
        "answer":"light"
    },
    "question18":{
        "question":"How many letters are in the English alphabet?....(Enter in number)",
        "answer":"26"
    },
    "question19":{
        "question":"What is the name of a shape with 5 sides?",
        "answer":"Pentagon"
    },
    "question20":{
        "question":"How many Continents are there?(Enter in number)",
        "answer":"7"
    },
    "question21":{
        "question":"What is the name of the tallest mountain on earth?",
        "answer":"Mount Everest"
    },
    "question22":{
        "question":"How many months have 31 days?....(Enter in number)",
        "answer":"7"
    },
    "question23":{
        "question":"How many colors of the rainbow are there?....(Enter in number)",
        "answer":"7"
    },
    "question24":{
        "question":"How many zeros are in ten thousand?....(Enter in number)",
        "answer":"4"
    },
    "question25":{
        "question":"My mother’s mother is my…what?",
        "answer":"Grandmother"
    }
}
score=0
for key,value in quiz.items():
    print(value["question"])
    answer=input("Answer?")

    if answer.lower()==value["answer"].lower():
        print("Correct")
        score=score+1
        
    else:
        print("Wrong")
        print("The answer is", value['answer'])

print("Your score is ",score)

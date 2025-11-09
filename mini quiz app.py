#mini quiz app with collections and random
import random
from collections import Counter
quiz=[
    
      
{"question":"What is the capital city of Mali?",
  "options":{"A":"Lesotho","B":"Bamako","C":"Harare","D":"Nairobi"},
  "answer":"B"
},
      
{"question":"Which planet has the most noons?",
  "options":{"A":"Mars","B":"Uranus","C":"Jupiter","D":"Saturn"},
  "answer":"D"
},

{"question":"What is the largest organ in the body?",
  "options":{"A":"Liver","B":"Heart","C":"Skin","D":"Spleen"},
  "answer":"C"
},

{"question":"What is acrophobia a fear of?",
  "options":{"A":"Heights","B":"small spaces","C":"spiders","D":"clowns"},
  "answer":"A"
},

{"question":"What is the fourth letter of the greek alphabet?",
  "options":{"A":"Omega","B":"Delta","C":"Alpha","D":"Phi"},
  "answer":"B"
}
]  


def run_quiz(quiz):
  score=[]
  for i, q in enumerate(quiz, 1):
    print(f"\nQ{i}: {q['question']}")
    for key, value in q["options"].items():
      print(f"{key}. {value}")

    answer=input("Please enter your choice:")
    if answer==q["answer"]:
      print("You answered correctly")
      score.append("correct")
    else:
      correct_answer = q['answer']
      print(f"You answered incorrectly, the correct answer is{correct_answer}. ({q['options'][correct_answer]})")
      score.append("wrong")
    summary=Counter(score)

  print(f"Your results for this quiz : You scored {summary['correct']} correctly and {summary['wrong']} wrongly")


if __name__=="__main__":
  run_quiz(quiz)


    
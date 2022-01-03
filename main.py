
import art
import random 
CORRECT_NUMBER = random.randint(1,100)
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5


def is_correct(user_guess):
  if user_guess == CORRECT_NUMBER:
    print(f"You got it! The answer was {CORRECT_NUMBER}. ")
    return True
  elif user_guess < CORRECT_NUMBER :
     print("Too Low.")
     return False
  elif user_guess > CORRECT_NUMBER:
    print("Too High.")
    return False

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if(difficulty == "hard"):
      return HARD_LEVEL_TURNS


def game():
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  print(f"Pssst, the correct answer is {CORRECT_NUMBER}")

  number_of_guesses_remaining = set_difficulty()

 
  finished = False

  while(not finished):
    print(f"You have {number_of_guesses_remaining} attempts remaining to guess the number.\n")

    number_of_guesses_remaining -=1

    user_guess = int(input("Make a guess : "))
    finished = is_correct(user_guess)
    if finished:
      return
    elif number_of_guesses_remaining > 0  :
      print("Guess Again.")
    else:
      print("You've run out of guesses, you lose.")
      return

    

game()
    


  





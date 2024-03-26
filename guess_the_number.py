import random


#global varibles for no of attempts as per difficulty
easy_difficulty_attempts=10
hard_difficuty_attempts=5

#function that returns number of attempts as per difficulty choosen
def set_difficulty(level):
    if level=="easy":
        return easy_difficulty_attempts
    else:
        return hard_difficuty_attempts

def check_answer(answer,guessed_number,attempts):
    if answer>guessed_number:
        print("your guess is too low!!")
        return attempts-1
    elif answer<guessed_number:
        print("your guess is too high!!")
        return attempts-1
    else:
        print(f"your guess is right...answer is {guessed_number}")

def game():
    print("\n************ THE NUMBER GUESSING GAME ************\n")
    level = input("choose difficulty level 'hard' or 'easy': ").lower()
    answer = random.randint(1, 50)
    attempts = set_difficulty(level)
    guessed_number = 0
    while guessed_number!=answer:
        print(f"\nyou have {attempts} chances remaining")
        guessed_number = int(input("make a guess: "))
        attempts = check_answer(answer, guessed_number, attempts)

        if attempts==0:
            print("you loose!!")
            return
        elif guessed_number!=answer:
            print("guess again")



game()
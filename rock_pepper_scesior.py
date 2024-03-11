from random import *

user_input=int(input('''enter valid option 
0-Rock
1-Paper
2-Scissor: '''))
computer_input_lst=["Rock","Paper","Scissor"]
k=len(computer_input_lst)-1
computer_choice=randint(0,k)
if user_input in [0,1,2]:
    print(f"computer choice is {computer_choice} which is {computer_input_lst[computer_choice]}")

    if computer_choice>user_input:
        if computer_choice==2 and user_input==0:
            print("You Won!!")
        else:
            print("You Loose!!")
    elif user_input>computer_choice:
        if user_input==2 and computer_choice==0:
            print("You Loose!!")
        else:
            print("You Won!!")
    else:
        print("Draw!!")
else:
    print("enter valid input")


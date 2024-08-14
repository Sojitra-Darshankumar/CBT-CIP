print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

print('Rock = 1\n'
      + "Paper = 2\n"
      + "Scissor = 3\n")


import random


while True:
    user_choise = int(input("Enter No : "))

    while user_choise > 3 or user_choise < 1:
        user_choise = int(input("invalid input\n Enter valid input : "))

    comp_choise = random.randint(1,3)

    if user_choise == 1:
        user_result = "Rock"
    elif user_choise == 2:
        user_result = "Paper"
    else:
        user_result = "Scissor"


    if comp_choise == 1:
        comp_result = "Rock"
    elif comp_choise == 2:
        comp_result = "Paper"
    else:
        comp_result = "Scissor"
    
    print("User Choise = ", user_result)
    print("Computer Choise = ", comp_result)


    if user_choise == comp_choise:
        result = "Draw"


    if user_choise == 1 and comp_choise == 2:
        print("@@@@@ Paper @@@@@")
        result = "Paper"
    elif user_choise == 2 and comp_choise == 1:
        print("@@@@@ Paper @@@@@") 
        result = "Paper"

    if user_choise == 1 and comp_choise == 3:
        print("@@@@@ Rock @@@@@")
        result = "Rock"
    elif user_choise == 3 and comp_choise == 1:
        print("@@@@@ Rock @@@@@")
        result = "Rock"

    if user_choise == 2 and comp_choise == 3:
        print("@@@@@ Scissor @@@@@")
        result = "Scissor"
    elif user_choise == 3 and comp_choise == 2:
        print("@@@@@ Scissor @@@@@")
        result = "Scissor"

    if result == "Draw":
        print("Match Draw")
    elif result == user_result:
        print("=> User Win <=")
    else:
        print("=> Computer Win <=")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
    else:
        continue

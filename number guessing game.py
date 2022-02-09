print("welcome to number guessing game")
print("-"*60)
import random
x = random.randint(1,100)
no_of_guess=0
max_guess =10

while no_of_guess<max_guess:
    user_guess=int(input("guess any number between 1 to 100 :"))
    if user_guess>x:
        print("try smaller number")
        print("-"*40)
        no_of_guess+=1
        print("remaining no of guesses : ",max_guess-no_of_guess)
        print("="*50)
    elif user_guess<x:
        print("try higher number")
        print("-" * 40)
        no_of_guess+=1
        print("remaining no of guesses : ", max_guess - no_of_guess)
        print("=" * 50)
    else:
        print("congratulation you win the game")
        print("it took ",no_of_guess," guess to win the game")
import random

print("Number Guessing Game")
print("Guess a number between 1-9")

chances=0
number= random.randint(1,9)

while chances < 5:
    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("CONGRATULATION YOU WIN!!!")
        break

    elif guess < number:
        print("guess a number higher", guess)
    else:
        print("guess a number lower than", guess)
    chances += 1
        
if not chances < 5:
        print("YOU LOSE, the number is", number)



   
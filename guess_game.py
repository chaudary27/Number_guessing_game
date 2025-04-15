import random
comp=random.randint(0,100)
print("NUMBER GUESSING GAME (guess a number between 1 and 100)")
guess=0
n=int(input("Enter your number: "))
while (n!=comp):
    n=int(input(f"you choosed {n} and this is a wrong guess.enter again "))
    if(n>comp):
        print("your guess is greater than number ")
    else:
        print("your guess is smaller than the number ")
    guess+=1
if(n==comp):
    print(f"you guessed the number in {guess} attempts" )

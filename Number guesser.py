import random

print("Welcome challenger")

a=input("Are you ready to guess the number ")
if a != "yes":
    quit()
chance=int(input("How many chances do you require? "))

if chance >5:
    print("Better you go play candy crush.....")
else:
    print("We move forward then....")
answer = random.randint(1,10)
for i in range(chance):
   
    guess = int(input("Enter your guess "))

    if guess == answer:
        print("Congratulations, you have guessed correctly")
        quit()
    elif guess > answer:
        print("Try going lower")
        
        
    elif guess < answer:
            print("Try going higher")
            
    if i==chance and guess != answer:
        print("Better luck next time")

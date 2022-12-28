print ("Welcome to the quiz")
a= input("Are you ready to play? ")
score = 0
if a != "yes":
    quit()
else:
    print("Let the game begin")

answer=input("What is the role of reyna? ")
if answer == "duelist":
    print("You have guessed correctly")
    score +=1
else:
    print("Wrong answer")

answer=input("What is the role of skye? ") 
if answer == "initiator":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")

answer = input("What is the role of raze? ")
if answer == "duelist":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")

answer = input("What is the role of sova? ")
if answer == "initiator":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")
answer = input("What is the role of brim? ")
if answer == "controller":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")    

answer = input("What is the role of omen? ")
if answer == "controller":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")    

answer = input("What is the role of harbour? ")
if answer == "controller":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")    

answer = input("What is the role of chamber? ")
if answer == "sentinel":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")    

answer = input("What is the role of sage? ")
if answer == "sentinel":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")    
answer = input("What is the best agent with best ultimate? ")
if answer == "chAMber":
    print("You have guessed correctly!")
    score +=1
else:
    print("Wrong Answer ")    

print("You guessed "+ str(score) + " questions correctly out of 10 questions")
print("The percentage of correct guesses are "+ str((score/10)*100) +"%" )
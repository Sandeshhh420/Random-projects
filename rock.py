a=input("Wanna play rock paper scissors? ")
if a != "yes":
    quit()
else:
    a=print("Alright, let's get the game started")
b=input("Are u a pathetic loser playing this alone? ")
if b == "yes":
    print("Noice")
else:
    print("Alright giga chads, let's begin")
for i in range(3):
    c1= input("Enter first choice ")
    c2=input("Enter second choice ")
    count=0
    count1=0
    if c1=="rock" and c2== "scissors" or c1== "scissors" and c2=="paper" or c1=="paper" and c2=="rock":
        print("Player 1 has won this round")
        count += 1
    elif c1== "scissors" and c2=="rock" or c1=="paper" and c2=="scissors" or c1=="rock" and c2=="paper":
        print("This round goes to player 2")
        count1 +=1
    else:
        print("Invalid entry")
if count > 2:
    print("Player 1 has won the game")
elif count1 > 2:
    print("Player 2 has emerged victorious")      
else:
    print("Disqualified")
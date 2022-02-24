print("Rock....")
print("Paper....")
print("Scissors....")

from random import randint

player = input("enter rock, paper, scissors or enter to quit: ")

rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
    
    
while player != "":

    print(f"Computer plays: {computer}")
    print(f"Player plays: {player}")

    if player == "rock" and computer == "scissors" :
        print("Player wins!")
    elif player == "rock" and computer == "paper" :
        print("Computer wins!")
    elif player == "paper" and computer == "rock" :
        print("Player wins!")    
    elif player == "paper" and computer == "scissors" :
        print("Computer wins!")
    elif player == "scissors" and computer == "rock":
        print("Computer wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    elif player == "rock" and computer == "rock":
        print("Tie!!!!")
    elif player == "paper" and computer == "paper":
        print("Tie!!!")
    elif player == "scissors" and computer == "scissors":
        print("Tie!!!!")        
    else:
        print("something went wrong")
        
    player = input("enter rock, paper, scissors or enter to quit: ")       
    rand_num = randint(0,2)
    
                    
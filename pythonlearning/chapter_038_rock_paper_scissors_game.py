import random

choices = ["rock","paper","scissors"]
play_again = "yes"

def game():

    # loop to prevent no/bad input
    player = None
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    # computer selects game choice
    computer = random.choice(choices)

    # calculate game result
    result = ""
    if player == computer:
        result = "tie"
    elif (player == "rock" and computer == "scissors")\
        or (player == "paper" and computer == "rock")\
        or (player == "scissors" and computer == "paper"):
            result = "player wins"
    else: result = "computer wins"

    # print game choices and outcome
    print("player: ",player)
    print("computer: ",computer)
    print("result: " + result)

# run game until player no longer says yes to play again
while play_again == "yes":
     game()
     
     play_again = ""

     # force yes/no answer to play again
     while play_again not in ["yes","no"]:
          play_again = input("Play again? (yes/no): ").lower()

# say goodbye
print("Goodbye!")
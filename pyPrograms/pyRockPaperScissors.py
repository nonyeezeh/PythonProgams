#imports
import time
import random

#intro
print("Rock...")
time.sleep(1)
print("Paper...")
time.sleep(1)
print("Scissors...")
time.sleep(1)
print("Shoot!\n")
time.sleep(2)

user_name = input("Enter your name: ")
time.sleep(1)
print("Hello, ", user_name, "\n")
time.sleep(1)

#score
points = 0

#instructions
choice = input("Type 'Y' to begin and 'X' to exit the game: ")
while(choice.lower() == 'y'):

    #computer generated random word
    computer = ["rock", "paper", "scissors"] #each computer guess stored in an array
    rand_index = random.randint(0, len(computer) - 1) #position of each word randomized
    rand_answer = computer[rand_index] #random computer answer stored

    #gameplay
    user_turn = input("Enter your answer - Rock, paper, or scissors? ")

    if(user_turn.lower() != "rock" and user_turn.lower() != "paper" and user_turn.lower() != "scissors" and user_turn.lower() != rand_answer):
        while(user_turn.lower() or "rock" or user_turn.lower() != "paper" and user_turn.lower() != "scissors" and user_turn.lower() != rand_answer):
            print("\nPlease make sure you spell your choice correctly.")
            user_turn = input("Enter your answer - Rock, paper, or scissors? ")
        
    #verdict
    if(user_turn == rand_answer):
        print("Your answer: ", user_turn,
            "\nComputer answer: ", rand_answer,
            "\nIt's a tie! No point.")
    elif(user_turn.lower() == "rock" and rand_answer == "paper"):
        print("Your answer: ", user_turn,
            "\nComputer answer: ", rand_answer,
            "\nYou lost.")
    elif(user_turn.lower() == "paper" and rand_answer == "rock"):
        print("Your answer: ", user_turn,
            "\nComputer answer: ", rand_answer,
            "\nYou won.")
        points += 1
    elif(user_turn.lower() == "rock" and rand_answer == "scissors"):
        print("Your answer: ", user_turn,
            "\nComputer answer: ", rand_answer,
            "\nYou won.")
        points += 1
    elif(user_turn.lower() == "scissors" and rand_answer == "rock"):
        print("Your answer: ", user_turn,
            "\nComputer answer: ", rand_answer,
            "\nYou lost.")
    elif(user_turn.lower() == "paper" and rand_answer == "scissors"):
        print("Your answer: ", user_turn,
            "\nComputer answer: ", rand_answer,
            "\nYou lost.")
    elif(user_turn.lower() == "scissors" and rand_answer == "paper"):
        print("Your answer: ", user_turn,
            "\nComputer answer: ", rand_answer,
            "\nYou won.")
        points += 1

    choice = input("Play again? Type 'Y' to begin and 'X' to exit the game: ")

time.sleep(1)
print("\nPoints: ", points, "\nBye!")
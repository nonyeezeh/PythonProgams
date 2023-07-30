#imports
import random
import time

#Introduction
print("Welcome to PyGuess - A Python Guessing Game!")
username = input("Enter your name: ")
time.sleep(1)
print("Hello, ", username)

#Instructions
print("Guess the correct number.")
time.sleep(1)
print("Between 1 and 10.")
time.sleep(1)
print("You have 5 guesses.")
time.sleep(1)
print("Goodluck!")
time.sleep(1)
print("Type 'X' to stop the game.")
time.sleep(1)
print("Type 'Q' to start the game.")
time.sleep(1)

choice = input("Choice: ")
while(choice.lower() == 'q'):
    #Generate random number
    number = random.randint(1,10)

    #List to store guesses
    guesses = []

    #Guess the number
    iteration = 1 #number of guesses used
    decrease = 5 #number of guesses left

    guess = int(input("\nGuess 1: "))
    if(guess < 1 or guess > 10):
        while(guess < 1 or guess > 10):
            time.sleep(1)
            print("Number out of bounds!")
            time.sleep(1)
            guess = int(input("\nGuess 1: "))

    if(guess >= 1 or guess <= 10):
        if(guess == number):
            time.sleep(1)
            print("Correct!")
            print("The secret number is ", number)

        else:
            while(guess != number and iteration != 5):
                decrease -= 1
                guesses.append(guess)
                time.sleep(1)
                print("Wrong! Try again. ", decrease, " more guesses.")
                iteration += 1
                print("Guess", iteration, ": ")
                guess = int(input())

                #Restrictions
                if(guess < 1 or guess > 10):
                    while(guess < 1 or guess > 10):
                        time.sleep(1)
                        print("Number out of bounds!")
                        time.sleep(1)
                        print("Guess", iteration, ": ")
                        guess = int(input())

                elif(guess == number):
                    time.sleep(1)
                    print("Correct! You got it after ", iteration, " guesses.")
                    time.sleep(1)
                    print("These are your guesses from smallest to largest: ")
                    guesses.sort()
                    time.sleep(1)
                    print(guesses)
                    print("The secret number is ", number)

            if(iteration == 5 and guess != number):
                guesses.append(guess)
                time.sleep(1)
                print("You did not get the number.")
                time.sleep(1)
                print("These are your guesses from smallest to largest: ")
                guesses.sort()
                time.sleep(1)
                print(guesses)
                time.sleep(1)
                print("The secret number is ", number)

    print("Would you like to play again, ", username, "?")
    choice = input("Choice ('Q' to play; 'X' to stop): ")


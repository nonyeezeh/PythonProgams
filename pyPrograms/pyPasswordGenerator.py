# imports
"""import random
import time

# instructions
time.sleep(1)
print("Generate a random password. All passwords are strong.")

# user details
time.sleep(1)
user_name = input("Enter your name: ")
time.sleep(1)
print("Hello, ", user_name)

# complexity
time.sleep(1)
print("\nThe following are the options for password complexity:")
time.sleep(1)
print("1 \nBasic: 5 - 8 characters \n Combination: lower- and upper-case letters only")
time.sleep(1)
print("2 \nIntermediate: 9 - 14 characters \n Combination: lower- and upper-case letters; numbers included")
time.sleep(1)
print("3 \nDifficult: 15 - 20 characters \n Combination: numbers; lower- and upper-case letters; special characters included")
time.sleep(2) """
psw_complexity = input("\nChoose the complexity of the password from the options displayed above: ")

# length
#if(psw_complexity != 1 or psw_complexity != 2 or psw_complexity != 3):
while(psw_complexity != 1 or psw_complexity != 2 or psw_complexity != 3):
    psw_complexity = input("Please enter a suitable password complexity from the options displayed above: ")

if(psw_complexity == 1):
    psw_length = input("\nChoose the length of the password between 5 - 8 characters: ")
elif(psw_complexity == 2):
    psw_length = input("\nChoose the length of the password between 9 - 14 characters: ")
elif(psw_complexity == 3):
    psw_length = input("\nChoose the length of the password between 15 - 20 characters: ")
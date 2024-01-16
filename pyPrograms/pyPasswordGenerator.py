# imports
import random
import time
import random
import string

# instructions
time.sleep(1)
print("Generate a random password. All passwords are strong.")

# user details
time.sleep(1)
user_name = input("Enter your name: ")
time.sleep(1)
print("Hello, ", user_name)

time.sleep(1)
choice = input("\nType 'Y' to begin and 'X' to exit the password generator: ")
while(choice.lower() == 'y'):

    # complexity
    time.sleep(1)
    print("\nThe following are the options for password complexity:")
    time.sleep(1)
    print("1 \nBasic: 5 - 8 characters \n Combination: lower- and upper-case letters only")
    time.sleep(1)
    print("2 \nIntermediate: 9 - 14 characters \n Combination: lower- and upper-case letters; numbers included")
    time.sleep(1)
    print("3 \nDifficult: 15 - 20 characters \n Combination: numbers; lower- and upper-case letters; special characters included")
    time.sleep(2)

    psw_complexity = int(input("\nChoose the complexity of the password from the options displayed above (1-3): "))

    # length
    if(psw_complexity != 1 and psw_complexity != 2 and psw_complexity != 3):
        while(psw_complexity != 1 and psw_complexity != 2 and psw_complexity != 3):
            print("Please enter a suitable password complexity from the options displayed above.")
            time.sleep(1)
            psw_complexity = int(input("Type option here: "))

    if(psw_complexity == 1):
        psw_length = int(input("\nChoose the length of the password between 5 - 8 characters: "))

        valid_lengths_1 = [5, 6, 7, 8]
        if psw_length not in valid_lengths_1: #create array to store valid answers
            while psw_length not in valid_lengths_1:
                print("Please enter a suitable password length as displayed above.")
                time.sleep(1)
                psw_length = int(input("Type option here: "))

        if 5 <= psw_length <= 8:
            #make sure to import 'string'. 'acii_letters' is also built-in apparently.
            character = string.ascii_letters
            # 'random.choice' specifically is used to make a random selection from a sequence (such as a list, tuple, or string). It is from the 'random' module.
            # create password
            password = ''.join(random.choice(character) for _ in range (psw_length))

            # create loaing illusion
            print("\nGenerating password ", end='', flush=True)
            for _ in range(3):
                time.sleep(1.5)
                print('.', end='', flush=True)
            
            # display password
            time.sleep(1.5)
            psw_com = "Password complexity is ", str(psw_complexity)
            psw_len = "Password length is ", str(psw_length)
            psw_actual = "Your password is ", password
            psw_info = psw_com + psw_len + psw_actual
            print("\n\n", psw_info)
            time.sleep(1.5)
            print("\nKeep it safe!")

            generated_pswds = []
            generated_pswds.append(psw_info)


    elif(psw_complexity == 2):
        psw_length = int(input("\nChoose the length of the password between 9 - 14 characters: "))

        valid_lengths_2 = [9, 10, 11, 12, 13, 14]
        if psw_length not in valid_lengths_2: #create array to store valid answers
            while psw_length not in valid_lengths_2:
                print("Please enter a suitable password length as displayed above.")
                time.sleep(1)
                psw_length = int(input("Type option here: "))

        if 9 <= psw_length <= 14:
            #make sure to import 'string'. 'acii_letters' is also built-in apparently.
            character = string.ascii_letters + string.digits
            # 'random.choice' specifically is used to make a random selection from a sequence (such as a list, tuple, or string). It is from the 'random' module.
            # create password
            password = ''.join(random.choice(character) for _ in range (psw_length))

            # create loaing illusion
            print("\nGenerating password ", end='', flush=True)
            for _ in range(3):
                time.sleep(1.5)
                print('.', end='', flush=True)
            
            # display password
            time.sleep(1.5)
            print("\n\nPassword complexity is: ", psw_complexity)
            print("Password length is ", psw_length)
            print("Your password is: ", password)
            time.sleep(1.5)
            print("Keep it safe!")

    elif(psw_complexity == 3):
        psw_length = int(input("\nChoose the length of the password between 15 - 20 characters: "))

        valid_lengths_3 = [15, 16, 17, 18, 19, 20]
        if psw_length not in valid_lengths_3: #create array to store valid answers
            while psw_length not in valid_lengths_3:
                print("Please enter a suitable password length as displayed above.")
                time.sleep(1)
                psw_length = int(input("Type option here: "))

        if 15 <= psw_length <= 20:
            #make sure to import 'string'. 'acii_letters' is also built-in apparently, as well as 'punctuation'
            character = string.ascii_letters + string.digits + string.punctuation
            # 'random.choice' specifically is used to make a random selection from a sequence (such as a list, tuple, or string). It is from the 'random' module.
            # create password
            password = ''.join(random.choice(character) for _ in range (psw_length))

            # create loaing illusion
            print("\nGenerating password ", end='', flush=True)
            for _ in range(3):
                time.sleep(1.5)
                print('.', end='', flush=True)
            
            # display password
            time.sleep(1.5)
            print("\n\nPassword complexity is: ", psw_complexity)
            print("Password length is ", psw_length)
            print("Your password is: ", password)
            time.sleep(1.5)
            print("Keep it safe!")
    
    choice = input("Generate again? Type 'Y' to begin and 'X' to exit the password generator: ")

print(generated_pswds)


#generate characters, long way around lol
'''
password = ""
for _ in range(psw_length): # '_' indicates that the variable will not necessarily be used in the loop.
    randletter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    randindex = random.randint(0, len(randletter) - 1)
    randgenerate = randletter[randindex]

    character = randgenerate
    
    password += character
'''
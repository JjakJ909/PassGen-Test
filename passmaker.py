# Jacob Jones
# 4/2025
# Password manager / generator application project
import random

components = []
scrambledat = []
new_dat = []
print("Looking to generate a password? You've come to the right place!")
print("lets get started...")



def passgenscramb():
 # asks for input and appends it to components
        passw = input("Type in something memorable, a date, name, time, etc to serve as your password base")
        components.append(passw)

#Asks for secondary inputs to act as the scrambled data, puts them into the scrambledat list
        while True:
            scram = input("Now give me another memorable input...")
            scrambledat.append(scram)
            check = input("Would you like to add another memorable input? (yes/no)")
            if check != 'yes':
                break
#prompts the user for which entry(s) they may want to scramble, lists them out from 0 onwards if multiple inputs
        print("\nWhich entry do you want to randomize?")
        for i, item in enumerate(scrambledat):
            print(f"{i}: {item}")
#asks for the entry numberprovided above
        select = int(input("Enter the number of the entry: "))

        choice = list(scrambledat[select])
        random.shuffle(choice)
        randomized = ''.join(choice)

#The newly randomized  input it appended to a new list. This randomized input will be combined later down the line
        new_dat.append(randomized)
        for item in new_dat:
            print("-", item)


        """print("These are your memorable inputs")
        for item in components:
            print("*", item)
        for item in scrambledat:
            print("-", item)"""












passgenscramb()

#def passgenread():


#def passgenwrite():


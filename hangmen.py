#modules to use for the game
import time
import random

#Asked for the username
name = input("Input your player name: ")
choice = False

#Different difficulties choice of words for the user to choose
ListOfDifficulties = [" ", "easy", "medium", "hard"]
EasyWords = ["listen", "phones", "games", "smile", "angry"]
MediumWords = ["janurary", "mysterious", "mission", "official", "heading"]
HardWords = ["azure", "blizzard", "buffalo", "cobweb", "banjo"]

print ("Hello, %s" % name, "Ready for a game of hangmen?")
#Delay the execution by 1.5 seconds to get the user ready
time.sleep(1.5)

#Ask user to select a difficulty
print("Select your difficulty, %s:" %name)
print("1. easy")
print("2. medium")
print("3. hard")

#A while loop for edge cases of when user did not input the numbers 1-3
while choice == False:
    difficulty = int(input("Enter your choice: "))

    if difficulty == 1 or difficulty == 2 or difficulty == 3:
        choice = True
    else:
        print("Invalid Input, Please Input Another Number")

#Generate a word by choosing a random number in the array
print("Generating a random", ListOfDifficulties[difficulty] + " word.")
time.sleep(1.5)

random = random.randint(0, 5)

#set the number of tries and word based on the difficulty
if(difficulty == 1):
    word = EasyWords[random]
    tries = 5
elif(difficulty == 2):
    word = MediumWords[random]
    tries = 9
elif(difficulty == 3):
    word = HardWords[random]
    tries = 13s

#initalize the user guess
guesses = ''

print("All done, start guessing %s." %name)

#A while loop that keeps running until the tries ran out
while tries > 0:
    #Update the word as the game progresses
    numberofDashes = 0
    for char in word:
        if char in guesses:
            print (char + ' ', end = ''),
        else:
            print ("_ ", end = ''),
            numberofDashes += 1

    print('\n')

    #end the loop if user guessed the word
    if numberofDashes == 0:
        print ('Nice Job %s , You guessed the word!' %name)
        break

    #Prompt user to guess a character in the "secret" word
    UserGuess = input("guess a character, %s: " %name)

    #add the character to the list of guesses
    guesses += UserGuess

    #if the guess is not in the word, reduce the number of tries
    if UserGuess not in word:
        tries -= 1
        print ('Wrong, guess again')

    #Update the user on how many tries they have left
    print ("You have", + tries, 'more guesses')

    #If ran out of tries, show game over and reveal the answer of the secret word
    if tries == 0:
        print ('Sorry %s ,' %name, 'You ran out of tries. The hidden word is %s' %word)

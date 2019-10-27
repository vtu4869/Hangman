import time

name = input("Input your player name: ")

print ("Hello, %s" % name, "Ready for a game of hangmen?")
time.sleep(2)

word = "python"

guesses = ''

turns = 10

while turns > 0:

    numberofDashes = 0
    for char in word:
        if char in guesses:
            print (char + ' ', end = ''),
        else:
            print ("_ ", end = ''),
            numberofDashes += 1

    print('\n')

    if numberofDashes == 0:
        print ('Nice Job %s ' %name)
        break

    UserGuess = input("guess a character, %s: " %name)

    guesses += Userguess

    if UserGuess not in word:
        turns -= 1
        print ('Wrong, guess again')

    print ("You have", + turns, 'more guesses')

    if turns == 0:
        print ('Sorry %s ,' %name, 'You ran out of turns the hidden word is %s' %word)

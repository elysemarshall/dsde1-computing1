
import random
print("Hello, What is your name?")
name = input()
print("Hi "+ name + " I am thinking of a number between 1 and 20. Guess what it is")
secretnumber = random.randint(1,20)

for guessestaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretnumber:
        print("Your guess is too low")
    elif guess > secretnumber:
        print("Your guess is too high")
    else:
        break

if guess == secretnumber:
    print("Good job, you guessed the number in " + str(guessestaken) + " guesses")
else: print("Nope, the number was " + str(secretnumber))


import random as rd

randNumber= rd.randint(1,100)
guesses= 0 
userGuess= None

 
while (userGuess != randNumber):
    userGuess= input("Enter your guess:") 
    guesses +=1

    try:
        userGuess=int(userGuess)
        if (userGuess==randNumber):
            print("You guessed it right!")
        else:
            if (userGuess>randNumber):
                print("You guessed it wrong! Enter a smaller number")
            else:
                print("You guessed it wrong! Enter a larger number")
    except Exception as e:
        print(e)
print(f"You guessed the no. in {guesses} guesses")
with open("highscore.txt","r") as f:
    highscore= int(f.read())
if (guesses<<highscore):
    print ("Yuo hsve just broken the high score!") 
    with open("highscore.txt","w") as f:
        f.write(str(guesses))

print(highscore)

'''Explaination of code:
This code is a simple number guessing game. It imports the `random` module as `rd` and generates a random number between 1 and 100 using the `randint()` function. It then initializes the `guesses` variable to 0 and `userGuess` to `None`.

The code then enters a `while` loop that continues until the user's guess matches the random number. Within this loop, the user is prompted to enter their guess using the `input()` function. The `guesses` variable is incremented by 1 for each guess.

The user's input is then converted to an integer using the `int()` function and checked against the random number. If the guess is correct, a message is printed to the console. If the guess is incorrect, the user is prompted to enter a smaller or larger number depending on whether their guess was too high or too low.

If the user's input cannot be converted to an integer, an error message is printed to the console.

Once the user has guessed the correct number, the code checks if their score is better than the current high score stored in a file called "highscore.txt". If it is, a message is printed to the console and the high score is updated in the file.

Finally, the code prints the current high score to the console.'''


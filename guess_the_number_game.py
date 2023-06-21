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


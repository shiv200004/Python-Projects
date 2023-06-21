import random #we imported a random function

#logic function of the game 
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp== 's':
        if you =='w':
            return False
        elif you == 'g':
            return True
    elif comp== 'w':
        if you =='g':
            return False
        elif you == 's':
            return True
    elif comp== 'g':
        if you =='s':
            return False
        elif you == 'w':
            return True
        


print("comp turn:Snake(s) Water(w) or Gun(g)?")
randno= random.randint(1,3)
if randno ==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

you=input("your turn: Snake(s) Water(w) or Gun(g)?")

a=gamewin(comp,you)

print(f"computer chose-{comp}")
print(f" you chose-{you} ")

if  a == None:
    print("the game is tie!")
elif a:
    print("you win!")
else:
    print("you lose!")
    
    
'''Explanation 
this Python code is a simple game of Snake, Water, and Gun. It uses the random function to generate the computer's 
choice and takes input from the user to determine their choice. The game logic is defined in the gamewin function, 
which returns True if the user wins, False if the computer wins, and None if it's a tie. The game's outcome is printed 
on the console, indicating the computer's and user's choices and whether the user has won, lost, or tied'''
 
   

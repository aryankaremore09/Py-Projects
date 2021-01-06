import random

def game():
    chances=1
    n=random.randint(1,100)
    while chances <=5:
        x=int(input("Guess any number : "))
        if x>n:
            if (x-n)<10:
                print("You are close, but the no. you guessed is greater!!!")
            else:
                print("The number you have guessed is too high!!!")
            chances+=1
            continue
        elif x<n:
            if (n-x)<10:
                print("You are close, but the no. you guesses is smaller!!!")
            else:
                print("The number you have guessed is too low!!!")
            chances+=1
            continue
        elif x==n:
            print("You win the game!!!")
            print("The number was : ",n)
            break
    if chances>5:
        print("\n \nYou ran out of chances , You lose!!!")
        print("The number was : ",n)
print("-------------------------------------------------NUMBER GUESSING GAME-------------------------------------------------")
game()
while input("Would to like to play again ? [Y for yes and N for no] : ")=='Y':
    game()
print("---------------------------------------------Thank u for playing----------------------------------------------------")
input("Press Enter to exit----")

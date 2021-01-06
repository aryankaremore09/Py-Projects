import random


def game():
    l=['Rock','Paper','Scissors']
    flag=True
    print("Lets test your luck!!!!")

    while flag:
        x=random.choice(l)
        choice=input("\nEnter your choice [rock / paper / scissors]: ")
        if choice.capitalize()==x:
            print("\nTry again!! its a tie!! ")
            print("\nYou chose",choice,"whereas computer chose",x)
            break
        elif choice.lower()=='rock' and x=='Paper':
            print("\nYou lose!!!")
            print("\nYou chose",choice,"whereas computer chose",x)
            break
        elif choice.lower()=='rock' and x=='Scissors':
            print("\nYou win!!!")
            print("\nYou chose",choice,"whereas computer chose",x)
            break
        elif choice.lower()=='paper' and x=='Rock':
            print("\nYou win!!!")
            print("\nYou chose",choice,"whereas computer chose",x)
            break

        elif choice.lower()=='paper' and x=='Scissors':
            print("\nYou lose!!!")
            print("\nYou chose",choice,"whereas computer chose",x)
            break
        elif choice.lower()=='scissors' and x=='Rock':
            print("\nYou lose!!!")
            print("\nYou chose",choice,"whereas computer chose",x)
            break
        elif choice.lower()=='scissors' and x=='Paper':
            print("\nyou win!!!")
            print("\nYou chose",choice,"whereas computer chose",x)
            break


print("-----------------------------------------------Welcome to Rock Paper Scissors-------------------------------------------------------")
game()

while input("\nDo you want to try again? Y for yes and N for no : ").upper()=='Y':
    game()
print("\n----------------------------------------------------Thank you for playing-------------------------------------------------------------")
input("\nPress Enter to quit....")

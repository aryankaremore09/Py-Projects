import random
choice=True
while choice==True:
    print(random.randint(1,6))
    q=input("Do you want to keep rolling?: y for yes and n for no : ")
    if q=='y':
        choice=True
    else:
        print("Thank you for rolling!!!")
        choice=False

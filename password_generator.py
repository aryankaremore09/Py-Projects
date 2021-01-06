import string
import random

alpha=[chr(x) for x in range(65,91)]+[chr(y) for y in range(97,123)]
num=[str(x) for x in range(0,10)]
sym=list(map(str,string.punctuation))
print("-----------------------------------------------WELCOME TO PASSWORD GENERATOR---------------------------------------------------")
plen=int(input("\nHow long do you want your password to be ? [min 6 characters are required] : "))
l,n=int(input("How many letters do you want? : ")),int(input("How many numbers do you want? : "))
password=random.sample(alpha,l)+random.sample(num,n)+random.sample(sym,(plen-l-n))
random.shuffle(password)
print("Your password is : ",''.join(password))
if input("Do you want to save your password for future reference ? Y for yes and N for no : ").lower()=='y':
    f=open('passwords.txt','a')
    f.write("\npassword : "+''.join(password))
    f.close()
    print("Your password has been saved!!!")
input("Press ENTER to quit")

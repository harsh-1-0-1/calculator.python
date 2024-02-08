import random
import string
n=int(input("give the lenght of password"))
print("this is a program for generating password ")
print("the generated password is " ,"".join(random.choices(string.ascii_letters+string.digits,k=n)))
#RANDOM PASSWORD GENERATOR

import string 
import random 

def gen(length):
    char =  string.ascii_letters + string.digits + string.punctuation 
    password = ""
    for i in range(length):
        password += (random.choice(char)) 
    return password
length=int(input("Enter number of digit of password = "))
print("Generated password = ", gen(length))

#importing random module for choice() method
import random

max_lenght = 8
password = ""
passchars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM0123456789"
print("Genrating password of "+str(max_lenght)+" characters")

for i in range(max_lenght):
    password = password + random.choice(passchars)

print("Password: " + str(password))
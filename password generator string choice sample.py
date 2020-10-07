#importing random module for choice() method
import random
max_length = 8
chars = "qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ1236547890"
password = ""
password2 = ""

print("Genrating password of "+str(max_length)+" characters")

#LOGIC 1
for i in range(max_length):
    password = password + random.choice(chars)

print("Password Logic 1: " + password)

#LOGIC 2
temp_pass = random.sample(chars, 8)
i = 0
for i in range(max_length):
    password2 = password2 + temp_pass[i]
print("Password Logic 2: " + str(password2))
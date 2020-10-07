#importing random module for choice() method
import random

cap = ['Q','W','E','R','T','Y','U','I','O','P','A','S','F','G','H','J','K','L','Z','X','C','V','B','N','M']
small = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
nums = ['1','2','3','4','5','6','7','8','9','0']
max_lenght = 8
password = ""
final_list = cap + small + nums

print("Genrating password of "+str(max_lenght)+" characters")

for i in range(max_lenght):
    password = password + random.choice(final_list)

print("Password: " + str(password))

#temp_pass = random.sample(final_list,8)
#for i in range(max_lenght):
#    password = password + temp_pass[i]

#print("Password: " + str(password))
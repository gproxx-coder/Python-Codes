import socket

c = socket.socket()

print("Client Socket Created")

c.connect(('localhost',9999)) #0 to 65535 port nos

client_name = input("Enter your name: ")

c.send(bytes(client_name,'utf-8'))

print(c.recv(1024).decode())  #Decode will not print the b (type of data sent by sever)
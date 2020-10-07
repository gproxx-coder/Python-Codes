import socket

s = socket.socket()

print("Server Socket Created")

s.bind(('localhost',9999)) #0 to 65535 port nos

s.listen(3)   #Accept max 3 connections

print("Waiting for connections")

while True:
    c, addr = s.accept() #gives client socket and address

    client_name = c.recv(1024).decode()

    print("Client connected with ",addr, client_name) #This will print IP add and Port no of client

    c.send(bytes("Welcome to GPz Laptop, {}".format(client_name),'utf-8'))

    c.close()
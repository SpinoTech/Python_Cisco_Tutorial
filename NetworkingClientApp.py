# this is the client file

import socket

s=socket.socket() # creating object of socket
host = socket.gethostname() # getting the local mechine name
port=12345

s.connect((host,port)) # for connecting to the server
print(s.recv(1024)) # client can receive upto 1024 byte 
s.close()
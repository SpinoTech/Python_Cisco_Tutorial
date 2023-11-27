#%% Networking in python %%

#$ connect with client & server -
#  * socket pogramming 
#  -> bi directional communication between server & client .  
#  -> socket client request to socket server 
#  -> server is listining the requests and responce back.



# this is the socket server file

import socket

s=socket.socket() # creating object of socket
host = socket.gethostname() # getting the local mechine name
port=12345
s.bind((host,port)) # binding the host and port no . (like ip + port)
s.listen(5) # it can responce 5 request (max quied connection)

while True :
    c,addr=s.accept()
    print("Got connection from ", addr)
    c.send(bytes('Thanks for connecting','utf-8'))
    c.close()

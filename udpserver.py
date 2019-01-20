#Matt Radiuk UDP Server

import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8889 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print( 'Socket created') 
 
s.bind((HOST, PORT))
     
print( 'Socket bind complete')
 
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
     
    reply = 'OK...' + data.decode()
     
    s.sendto(reply.encode() , addr)
    print( 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip().decode())
     
s.close()
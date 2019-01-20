import socket
import sys 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
host = "192.168.1.74"
port = 8889

while(1):
    msg = input('Enter message to send : ')
    s.sendto(msg.encode(), (host, port))
    d = s.recvfrom(1024)
    reply = d[0]
    addr = d[1]
         
    print ('Server reply : ' + reply.decode())

sys.exit()
     

#pingclient.py
#Matt Radiuk 2018 V00876753
from socket import *
import datetime
import time

serverName = "10.0.0.1"
port = 6789

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(1,11):
	startTime = time.time()
	message = "ping " + str(i) + " " + str(time.time())
	clientSocket.sendto(message.encode(), (serverName, port))

	try:
		data = clientSocket.recvfrom(1024)
		print(data[0].decode())
		RTT = ((time.time()) - startTime)
		print("     RTT: " + str(RTT))
	except timeout:
		print("Request timed out")
print("10 packets sent; that's all")


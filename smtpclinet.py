from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.uvic.ca', 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO mattyr\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM: <mattyr@uvic.ca>\r\n')
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
clientSocket.send('RCPT TO: <mattrdk2@gmail.com>\r\n')
recv3 = clientSocket.recv(1024)
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response. 
clientSocket.send('DATA\r\n')
recv4 = clientSocket.recv(1024)
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
clientSocket.send("subject: CSC 361\r\n")
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n')
recv6 = clientSocket.recv(1024)
print(recv6)
clientSocket.close()
clientSocket.close()
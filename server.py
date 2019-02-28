from socket import *
import sys 
host = ''
port = 6789

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(5)
x = gethostbyname(gethostname())
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept()

    try:
        #Revieves the request and sends the appropriate file  
        message = connectionSocket.recv(1024).decode()          
        filename = message.split()[1]               
        f = open(filename[1:]) 
        data = []
        for line in f.read().split("\n"):
            data.append(line)
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(data)):       
            connectionSocket.send(data[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()

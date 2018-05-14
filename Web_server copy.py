# Import socket module
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start

serverPort = 6789
print ("hostname is: ", gethostname() )
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Fill in end

while True:
	#Establish the connection
    print ("Ready to serve...")

	# Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept() #Fill in start   #Fill in end
    
    try:
        message =  connectionSocket.recv(1024) #Fill in start #Fill in end
        print ("message is :", message)
        filename = message.split()[1]
        print (" file name is :", filename)
        f = open(filename[1:])

        outputdata = f.read()#Fill in start #Fill in end
        out = outputdata.decode()
		#Send one HTTP header line into socket
		#Fill in start
        connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", "UTF-8"))
        
		#Fill in end

		# Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(out[i])
            connectionSocket.send("\r\n")
        connectionSocket.close()
            
    except IOError:
		# Send HTTP response message for file not found
		#Fill in start
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
		#Fill in end

		# Close the client connection socket
		#Fill in start
        connectionSocket.close()
		#Fill in end

serverSocket.close()

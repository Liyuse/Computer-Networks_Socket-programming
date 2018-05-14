from socket import *
import time

#Create a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 6789))
clientSocket.settimeout(1)


server_addr = 'localhost'
server_port = 12000

#loop in the range of 0 to 10
for i in range(0, 10):
    
    sendingtime = time.time()
    order = i
    message = "%s %d %s" % ('Ping', order, sendingtime)
    clientSocket.sendto(message.encode('utf-8'), (server_addr, server_port))

    try:
        recv, add = clientSocket.recvfrom(1024)
        roundtime = time.time() - sendingtime
        
        print("Received: %s Round: %f seconds" % (recv.decode(), roundtime))

    except OSError as error:
        #Send UDP response message for failed
        print("Request times out\n")

clientSocket.close()


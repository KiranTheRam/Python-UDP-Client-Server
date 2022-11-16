import socket

msgFromClient = "Hello there, UDP Listner"

# Encoding message to be sent
bytesToSend = str.encode(msgFromClient)

# Defining the address and port of the server.
# Matching the server's buffer size
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP client socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send data to server using client UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

# Receive a message from the server
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
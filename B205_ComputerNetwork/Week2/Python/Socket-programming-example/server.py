#P15/1898/2022
#Ian Samoei Kipchirchir
#Date: 10/6/2024

#The server script is used to create a server that listens for incoming connections from clients and 
# process the messages sent by the clients. 
# The server is able to handle multiple clients concurrently by creating a new thread for each client connection. 
# The server uses a fixed header length to determine the length of the incoming message and processes the message by reversing and 
# capitalizing it before sending it back to the client. 
# The server also checks for a disconnect key to close the connection with the client.
#  The server script is designed to run on the host machine's local IP address,
#  but it can automatically detect and use the local IP address if the specified IP address is unreachable. 
# The server script is implemented using the socket module in Python and can be run as a standalone script to create a server
#  that listens for incoming connections from clients.
import socket
import threading
import os

#Port that the server will be running
PORT=6550
# My local IP address so that it can be used to communicate with other devices in the LAN
local_ip="192.168.0.11"
#Set the server Ip to the same one as 
SERVER=local_ip
#Set the header to tell the length of the incoming message
HEADER=64
#Format of the header
FORMAT='utf-8'
#Key-word for disconnection
DISCONNECT_KEY="TSCHUSS!"
#check if the ip address is reachable, otherwise automatically use the one running in the host machine
ret = os.system(f"ping -n 1 {local_ip}")
# Check if the return value is 0 (indicating the ping was successful)
if ret != 0:
   #To automatically set the IP address from the host computer
   SERVER=socket.gethostbyname(socket.gethostname())

print(SERVER)
#Create the socket
server=socket.socket(socket.AddressFamily.AF_INET,socket.SOCK_STREAM)
ADDR=(SERVER,PORT)
server.bind(ADDR)
#Function to process the message received
def process_message(message):
    #Reverse and capitalize the message
    return message[::-1].upper()

#Function to handle the connection
def handle_conn(connection, address):
    print(f"[CONNECTION MADE]: {address}")
    connected_status = True
    while connected_status:
        try:
            # Receive the header and decode it
            header_data = connection.recv(HEADER)
            if not header_data:
                print(f"[DISCONNECTED] {address} has closed the connection.")
                break
            message_len = int(header_data.decode(FORMAT))
            if message_len:
                message = connection.recv(message_len).decode(FORMAT)
                print(f"{address} -> {message}")
                #To send the message back to the client in the same format
                response = process_message(message) 
                response_length = len(response)
                response_length = str(response_length).encode(FORMAT)
                connection.send(response_length)
                connection.send(response.encode(FORMAT))
                if message == DISCONNECT_KEY:
                    break
        except ValueError:
            print("Error decoding the message length")
        except OSError as e:
            print(f"[ERROR] {e} - Connection might be closed by client {address}")
            break
    connection.close()
    print(f"[CONNECTION CLOSED]: {address}")

      
def start_server():
   #Start the server
   server.listen()
   #Persistent Connection
   while True:
      #Unpack the connection tuple
      conn,addr=server.accept()
      thread=threading.Thread(target=handle_conn,args=(conn,addr))
      thread.start()
      print(f"[Connections] {threading.active_count()-1}")

if __name__=="__main__":
   print("Starting server")
   start_server()


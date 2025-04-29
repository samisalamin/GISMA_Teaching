#P15/1898/2022
#Ian Samoei Kipchirchir
#Date: 10/6/2024
import socket
#Set the header to tell the length of the incoming message
HEADER=64
#Format of the header
FORMAT='utf-8'
#Key-word for disconnection
DISCONNECT_KEY="TSCHUSS!"
PORT=6550
SERVER=socket.gethostbyname(socket.gethostname())
#Create the socket
client=socket.socket(socket.AddressFamily.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER,PORT))

def process_response(connection,address):
    #Use the same Protocol as the server, first check if there is a header
    try:
        # Receive the header and decode it
        header_data = connection.recv(HEADER)
        if not header_data:
            print(f"[DISCONNECTED] {address} has closed the connection.")
        message_len = int(header_data.decode(FORMAT))
        if message_len:
            message = connection.recv(message_len).decode(FORMAT)
            print(f"{address} -> {message}")
    except ValueError:
            print("Error decoding the message length")

def send_message(message):
    message = message.encode(FORMAT)
    message_length=len(message)
    message_length=str(message_length).encode(FORMAT)
    #pad the message length to the header length
    message_length+=b' '*(HEADER-len(message_length))
    client.send(message_length)
    client.send(message)
    process_response(client,SERVER)


def start_client():
    while True:
        message = input("Enter the message: ")
        send_message(message)
        if message == DISCONNECT_KEY:
            print("Closing the connection")
            break

    client.close()  

if __name__ == "__main__":
    start_client()
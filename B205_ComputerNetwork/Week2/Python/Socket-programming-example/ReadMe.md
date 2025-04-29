# TCP-IP Inter-Process Communication

## Table of Contents
- [TCP-IP Inter-Process Communication](#tcp-ip-inter-process-communication)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction
This code focuses on inter-process communication using the TCP/IP protocol. It utilises the `socket` module in python to send 
and receive data between two processes i.e. a server and a client. The server listens for incoming connections and the client sends a message to the server
The server then processes that message by reversing and capitalising it then returns a response to the client. The client then prints the response on the console.

## Installation
To set up the project, follow these steps:
1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    e.g.
    ```sh
    cd TCP-IP-Inter-Process-Communication
    ```

## Usage
To run the project, use the following command:
```sh
py server.py
```
and in another terminal run:
```sh
py client.py
```
You should see the following output:
<br>
For the server:
```sh
Pinging 192.168.0.11 with 32 bytes of data:
Reply from 192.168.0.11: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.0.11:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
192.168.0.11
Starting server
```
For the client:
```sh
Enter the message:
```
Once you see the above output, you can enter a message and press enter. The server will process the message and return a response to the client. The client will then print the response on the console.
e.g
```sh
Enter the message: Hello
Server response-> OLLEH
```
To stop the server, press `Ctrl+C` in the terminal where the server is running.
<br>

**Note:**
Ensure that you have the necessary environment set up for network communication.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Link to my Repo
[My Repo](https://github.com/Mansafreo/TCP-IP-Socket-in-Python)

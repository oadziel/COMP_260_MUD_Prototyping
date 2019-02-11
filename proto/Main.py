import socket

if __name__ == '__Main__':
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mySocket.connect(("127.00.1", 8222))

    testString = "This is a message from the Client"

    mySocket.send(testString.encode())

    while True:
        data = mySocket.recv(4096)
        print(data.decode("utf-8"))


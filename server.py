import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))
server.listen()
client, addr = server.accept()
while True:
    message = client.recv(1024).decode('utf-8')
    if message == "quit":
        client.send("quit".encode('utf-8'))
        print("Client:", message)
        break
    print("Client:", message)
    client.send(input("Server: ").encode('utf-8'))

server.close()
client.close()
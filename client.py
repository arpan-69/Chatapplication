import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9999))
while True:
    client.send(input("Client: ").encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    if message == 'quit':
        break
    print("Server:",message)
client.close()
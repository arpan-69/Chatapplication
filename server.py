import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))
print("Server is listening...")
server.listen()
client, addr = server.accept()

while True:
    message = client.recv(1024).decode('utf-8')
    if message == "quit":
        print("Client has requested to end the chat.")
        client.send("quit".encode('utf-8'))
        break  # Exit the loop and stop receiving messages
    print("Client:", message)
    response = input("Server: ")
    if response == "quit":
        client.send("quit".encode('utf-8'))
        break  # Server decides to end the chat
    client.send(response.encode('utf-8'))
client.close()
server.close()
print('Server closed.')

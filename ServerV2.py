import socket
import threading

host = '192.168.0.46'  # 192.168.100.156
port = 3389

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:                                                            # receiving valid messages from client
            message = client.recv(1024)
            broadcast(message)
        except:                                                         # removing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('--{} left!--'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            print(f"'{nickname}': Disconnected")
            break


def receive():                                                          # accepting multiple clients
    while True:
        client, address = server.accept()
        client.send('Connected to server!'.encode('utf-8'))
        # print("Connected with {}".format(str(address)), end="")
        # client.send('NICKNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        print(f"'{nickname}': Connected from {str(address)}")
        broadcast("--{} joined!--".format(nickname).encode('utf-8'))
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server Started")
receive()

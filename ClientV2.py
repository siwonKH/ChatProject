import socket
import threading
import time


nickname = input("Choose your nickname: ")
nickname_len = len(nickname)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # socket initialization
client.connect(('218.158.89.141', 3389))                             # connecting client to server


def receive():
    while True:                                                 # making valid connection
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'Connected to server!':
                client.send(nickname.encode('utf-8'))
            else:
                if not message.startswith(nickname + ": "):
                    back = "\b" * (nickname_len + 70)
                    print(back, end="")
                    print(message, end=f"\n{nickname}<you>: ")

        except Exception as e:                                                 # case on wrong ip/port details
            print("An error occurred!")
            print(f"ERROR: {e}")
            time.sleep(10)
            client.close()
            break


def write():
    while True:                                                 # message layout
        print(f'{nickname}<you>: ', end="")
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)               # receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   # sending messages
write_thread.start()

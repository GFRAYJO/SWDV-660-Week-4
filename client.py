import socket

HOST = socket.gethostname() 
PORT = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))

    msg = input("Type a word: ").encode()
    c.send(msg)

    serv = c.recv(1024).decode()

    print(serv)
    c.close()
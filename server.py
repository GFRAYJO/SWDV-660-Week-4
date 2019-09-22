import socket

HOST = socket.gethostname() 
PORT = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv:
    serv.bind((HOST, PORT))
    serv.listen(5)
    serv, addr = serv.accept()

    print("Socket is up and running with a connection from",addr)

    while True:
        rcvdata = serv.recv(1024).decode()
        if (rcvdata == "Hello" or rcvdata == "hello"):
            resp = ("Hi!").encode()
            serv.send(resp)

        else:
            resp = ("Goodbye!").encode()
            serv.send(resp)
        
        if not rcvdata:
            break

serv.close()
              
        
   
    
import socket

# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = ''

# binding to the host and port
sock.bind((host, port))

# Accepts up to 10 connections
sock.listen(10)
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    con, address = sock.accept()
    print('Connected with ', address)

    data = con.recv(1024)

    # Read File in binary
    file = open('server-file.txt', 'rb')
    line = file.read(1024)

    while(line):
        con.send(line)
        line = file.read(1024)
    
    file.close()
    print('File has been transferred successfully.')

    con.close()

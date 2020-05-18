#https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php

# 40.113.193.118 vm1
# 40.77.109.130 vm2
# 40.86.72.115 vm3


import socket                   # Import socket module

port = 80                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from'), addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='dummydaya50MB.zip'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()
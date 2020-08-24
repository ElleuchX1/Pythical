import socket
C_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port=1111
C_socket.connect(('yourhost',port))
mess= C_socket.recv(1024) #maxdata 1024
C_socket.close()
print(mess.decode('ascii'))

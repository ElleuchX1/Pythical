import socket
s_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1111
s_socket.bind(('yourhost',port))

s_socket.listen(3)

while True:
    C_socket,address = s_socket.accept()
    print("Connection recieved: "+ str(address))
    mess='Hello,You are connected to the server '+'\n' 
    C_socket.send(mess.encode('ascii'))

    C_socket.close()
#DOC|USEFUL INFORMATIONS
# ------------------------------------------------------------------------------------#
# Socket/Address Family can be : 
# SAUCE: // IBM KNOWLEDGE CENTER //
# AF_INET : interprocess communication between processes that run on the same system or on different systems
# AF_INET6: provides support for the Internet Protocol version 6 (IPv6). AF_INET6 address family uses a 128 bit (16 byte) address.
# AF_UNIX : provides interprocess communication on the same system that uses the socket APIs. The address is actually a path name to an entry in the file system.
# AF_UNIX_CCSID: compatible with the AF_UNIX address family and has the same limitations.
# ------------------------------------------------------------------------------------#
# Socket Typecan be :
# SAUCE: // ORACLE DOCS // 
# SOCK_STREAM = Stream sockets allow processes to communicate using TCP
# SOCK_DGRAM = Datagram sockets allow processes to use UDP to communicate
# SOCK_RAW = Raw sockets provide access to ICMP
# ------------------------------------------------------------------------------------#


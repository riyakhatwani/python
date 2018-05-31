import socket
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
 msg=raw_input("enter the message :")
 x.sendto(msg,("127.0.0.1",8888))
 print x.recvfrom(100)

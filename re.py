import socket 
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("127.0.0.1",8888))
while 4>2:
 data=x.recvfrom(1000)
 print data[0]
 reply=raw_input("plz reply ur msg:")
 x.sendto(reply,data[1])

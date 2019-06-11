#! /usr/bin/python2
import socket
recv_ip="127.0.0.1"
recv_port=8889 # 0-1024 ---you can check udo port by using netstat -nulp
               #for tcp :- netstat -ntlp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
               #fitting ip and port with UDP-socket
s.bind((recv_ip,recv_port))
               #recieve data from sender
data=s.recvfrom(100) #here 100 shows maximum length of character supports in one short  of data streaming
print(data)

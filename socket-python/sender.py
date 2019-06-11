#! /usr/bin/python2
import socket
recv_ip="127.0.0.1"
recv_port=8889 # 0-1024 ---you can check udo port by using netstat -nulp
               #for tcp :- netstat -ntlp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
               #fitting ip and port with UDP-socket
s.bind((recv_ip,recv_port))
               #send data to reciever
s.sendto("hello theseus is back!",(recv_ip,recv_port))

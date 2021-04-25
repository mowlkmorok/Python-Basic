import socket 

ports = [21, 22, 23, 80, 443, 8080]
for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	cod = client.connect_ex(('192.168.1.1', port))
	if cod == 0:
		print(port, 'OPEN')


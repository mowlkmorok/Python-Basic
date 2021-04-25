import socket
import subprocess

#port = int(input())

#while port < 10:
#    print(port)
#    port = port + 1
#ping = socket.socket(socket.AF_INET, socket.SOCK_STREAM

def xx():
    port = range(100, 105) 
    for a in port:
        print(a)

#ping = socket .socket(socket.AF_INET, socket.SOCK_STREAM)

for a  in range(100, 105):
    ips = "192.168.0." + str(a)
    response = subprocess.call(['ping', '-n', '1', ips])
    
    if response == 0:
        print("ping to", ips, "OK")
    elif response == 2:
        print("No responsr from", ips)
    else:
        print("Ping to", ips, "Falied")

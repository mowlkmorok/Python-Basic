import subprocess

for a in range(100, 105):  #Range of IP
    ips = "192.168.0." + str(a)
    x = subprocess.call(['ping', '-n', '1', ips ])
    print(x)

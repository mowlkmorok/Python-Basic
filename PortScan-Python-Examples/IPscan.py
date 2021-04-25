import subprocess

for a in range(100, 105):  # IP Range
    ips = "192.168.0." + str(a)
    x = subprocess.call(['ping', '-n', '1', ips ])
    print(x)

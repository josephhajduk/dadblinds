from telnetlib import Telnet
import time

tn = Telnet('192.168.2.227', 9621)
tn.write("VERSION".encode("ascii")+b"\r")
response = tn.read_until(b"\r")
print(response)
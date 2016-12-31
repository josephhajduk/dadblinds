#!/usr/bin/env python3
from telnetlib import Telnet
import sys
import time

if len(sys.argv) == 2:
    tn = Telnet('192.168.2.227', 9621)
    print(sys.argv[1])
    tn.write(sys.argv[1].encode("ascii")+b"\r")
    response = tn.read_until(b"\r")
    print(response)
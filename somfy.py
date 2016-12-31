#!/usr/bin/env python3
import serial, sys
import time

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

for arg in sys.argv[1:]:
    print("SENDING: "+arg)
    ser.write((arg+"\r").encode())
    time.sleep(.1)


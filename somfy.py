#!/usr/bin/env python3
from aiohttp import web
import serial, sys
import time
import asyncio
from telnetlib import Telnet

@asyncio.coroutine
def rus(request):
    command = request.match_info.get('command', "VERSION").replace("_"," ")#.encode("ascii","ignore")
    commands = command.split("|")
    print("RUS COMMAND:"+str(commands))

    tn = Telnet('192.168.2.227', 9621)

    response = ""

    for com in commands:
        tn.write(com.encode("ascii","ignore")+b"\r")
        response += tn.read_until(b"\r", timeout=10).decode("ascii")+"\n"

    tn.close()
    response_str = response
    print("RESPONSE: "+response_str)
    return web.Response(text=response_str)


@asyncio.coroutine
def down(request):
    motor = request.match_info.get('motor', "01")
    print("MOTOR:"+motor+" COMMAND: DOWN")
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.write(("01"+motor+"D\r").encode())
    ser.close()
    return web.Response(text="DOWN")

@asyncio.coroutine
def up(request):
    motor = request.match_info.get('motor', "01")
    print("MOTOR:"+motor+" COMMAND: UP")
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.write(("01"+motor+"U\r").encode())
    ser.close()
    return web.Response(text="up")

@asyncio.coroutine
def stop(request):
    motor = request.match_info.get('motor', "01")
    print("MOTOR:"+motor+" COMMAND: STOP")
    print(motor)
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.write(("01"+motor+"S\r").encode())
    ser.close()
    return web.Response(text="up")

app = web.Application()
app.router.add_route("POST", '/{motor}/up', up)
app.router.add_route("POST", '/{motor}/down', down)
app.router.add_route("POST", '/{motor}/stop', stop)
app.router.add_route("GET", '/rus/{command}', rus)
app.router.add_route("POST", '/rus/{command}', rus)

web.run_app(app)
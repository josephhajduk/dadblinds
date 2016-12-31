from aiohttp import web
import serial, sys
import time
import asyncio

@asyncio.coroutine
def down(request):
    motor = request.match_info.get('motor', "01")
    print(motor)
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
    print(motor)
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

@asyncio.coroutine
def myposition(request):
    motor = request.match_info.get('motor', "01")
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
    time.sleep(.1)
    ser.write(("01"+motor+"S\r").encode())
    ser.close()
    return web.Response(text="myposition")

app = web.Application()
app.router.add_route("POST", '/{motor}/up', up)
app.router.add_route("POST", '/{motor}/down', down)
app.router.add_route("POST", '/{motor}/myposition', myposition)
app.router.add_route("POST", '/{motor}/stop', stop)

web.run_app(app)
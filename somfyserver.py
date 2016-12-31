from aiohttp import web
import serial, sys
import time

async def down(motor):
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

async def up(motor):
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

async def stop(motor):
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

async def myposition(motor):
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

web.run_app(app)
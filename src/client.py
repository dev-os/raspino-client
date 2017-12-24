#!/usr/bin/env python3

import subprocess
import serial

def main():
    #subprocess.run("echo \"Hello World\"", shell=True, check=True)
    ser = serial.Serial(
    port = "/dev/ttyUSB0",
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    bytesize = serial.EIGHTBITS,
    stopbits = serial.STOPBITS_ONE,
    timeout = None,
    xonxoff = 0,
    rtscts = 0,
    )

    ser.write(b"1145141919810###")
    while True:
        print(ser.read().decode('utf-8'))

    ser.close()

if __name__ == '__main__':
    main()

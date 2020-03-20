import serial
import time

s = serial.Serial('COM3', 9600, timeout=1)

while True:
    s.write(b'T')
    res = s.readline()
    if res:
        value = float(res)
        print(value)
    time.sleep(1)
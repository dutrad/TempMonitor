import time

from serialPort import serial_ports
from serial import Serial

s_port: str = serial_ports()
if s_port:
    print(s_port + ' will be used')
else:
    print('No serial port found')
    exit()

s = Serial(s_port, 9600, timeout=1)

while True:
    s.write(b'T')
    res = s.readline()
    if res:
      try:
         temp = float(res)
         print(temp)
         time.sleep(1)

      except (KeyboardInterrupt, SystemExit):
         raise
      except:
         raise


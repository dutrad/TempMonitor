import time as t
import urllib.parse
import urllib.request

from serial import Serial, SerialException
from serialPort import serial_ports

def firstTemps(serialp):
    y0,y1 = 0.0
    
    while True:
       serialp.write(b'T')
       line = serialp.readline()

       if line:
           if y0 == 0.0:
              y0 = float(res)
              print(t0)
              y1 = float(res)
              print(t1)
              return [y0,y1]

s_port: str = serial_ports()
while s_port == "":
    t.sleep(5)
    print('No serial port found')
    s_port = serial_ports()

print(s_port + ' will be used')

s = Serial(s_port, 9600, timeout=1)
apiKey: str = '1VP9BWGNWA91KDHU'

[t0,t1] = firstTemps(s)

while True:
    s.write(b'T')
    res = s.readline()
    if res:
        temp = (float(res) + t0 + t1)/3
        print(temp)

        t0 = t1
        t1 = temp

        try:
            params = urllib.parse.urlencode({'key': apiKey, 'field1': temp}).encode('ascii')
            f = urllib.request.urlopen("https://api.thingspeak.com/update", data=params)

            t.sleep(30)
        except (KeyboardInterrupt, SystemExit):
            raise
        except (OSError, SerialException):
            pass
        except:
            print('Error sending temperature to Thingspeak')

import time as t
import urllib.parse
import urllib.request

from serial import Serial, SerialException
from serialPort import serial_ports

def firstTemps(serialP):
    t0,t1 = 0.0
    while True:
       serialP.write(b'T')
       res = serialP.readline()
      
       if res:
           if t0 == 0.0
              t0 = float(res)
              print(t0)
           else
              t1 = float(res)
              print(t1)
              return [t0,t1]

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

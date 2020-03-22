import glob
import sys
import time
import urllib.parse, urllib.request

import serial


def serial_ports():
    """ Find serial port

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    for port in ports:
        try:
            se = serial.Serial(port)
            se.close()
            return port
        except (OSError, serial.SerialException):
            pass

    return ""


s_port: str = serial_ports()
if s_port:
    print(s_port + ' will be used')
else:
    print('No serial port found')
    exit()

s = serial.Serial(s_port, 9600, timeout=1)
apiKey: str = '1VP9BWGNWA91KDHU'

while True:
    s.write(b'T')
    res = s.readline()
    if res:
        temp = float(res)
        print(temp)

        params = urllib.parse.urlencode({'key': apiKey, 'field1': temp}).encode('ascii')
        f = urllib.request.urlopen("https://api.thingspeak.com/update", data=params)

    time.sleep(60)

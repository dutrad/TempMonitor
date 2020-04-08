import glob
import sys
import time as t
import urllib.parse
import urllib.request

from serial import Serial, SerialException


def serial_ports() -> str:
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
            se = Serial(port)
            se.close()
            return port
        except (OSError, SerialException):
            pass

    return ""


s_port: str = serial_ports()
while s_port == "":
    t.sleep(5)
    print('No serial port found')
    s_port = serial_ports()

print(s_port + ' will be used')

s = Serial(s_port, 9600, timeout=1)
apiKey: str = '1VP9BWGNWA91KDHU'

while True:
    s.write(b'T')
    res = s.readline()
    if res:
        temp = float(res)
        print(temp)

        try:
            params = urllib.parse.urlencode({'key': apiKey, 'field1': temp}).encode('ascii')
            f = urllib.request.urlopen("https://api.thingspeak.com/update", data=params)

            t.sleep(300)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print('Error sending temperature to Thingspeak')

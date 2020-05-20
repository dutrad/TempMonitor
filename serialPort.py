import sys
import glob

from serial import Serial, SerialException


def serial_ports() -> str:
    """ Find serial port

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            The first serial port available
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



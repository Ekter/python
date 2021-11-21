import termios
import arduinoserial
serial_port=arduinoserial.SerialPort("COM3",9600)
while not(False):
    print(serial_port.read_until())

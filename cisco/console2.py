import serial
import time

print "Welcome to zero touch initial configuration"
time.sleep(1)
print "\n\n\n"
serialport = raw_input("Enter serial port: ")
time.sleep(1)

console = serial.Serial(
	port = '{}'.format(serialport),
	baudrate = 9600,
	parity = 'N',
	stopbits = 1,
	bytesize = 8,
	timeout = 8
	)

console.isOpen()
print "connection serial is open\n"
print "please select configuration bellow :"
print "1. IP address"
print "2. Credentials"
print "3. Routing"

choice = raw_input("Enter number configuration: ")
option = y

while option == y:
	interface = raw_input("Enter the interface of Router/Switch: ")
	address = raw_input("Enter IP for this interface: ")
	netmask = raw_input("Enter Subnetmask for this interface: ")
	
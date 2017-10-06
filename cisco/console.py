import serial
import time

print '#############################################'
print '#Welcome to zero touch initial configuration#'
print '#############################################'
time.sleep(1)
print '\n\nplease input parameter bellow'


console = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 9600,
	parity = 'N',
	stopbits = 1,
	bytesize = 8,
	timeout = 8
	)

console.write("\r\n\r\n")
time.sleep(1)

input_data = console.read(console.inWaiting())
if '#' in input_data:
	print "Exiting from priviledge mode"
	console.write('end\n')
	console.write('exit\n')
	time.sleep(1)

username = raw_input('Enter Your Username : ')
password = raw_input('Enter Your Password : ')
interface = raw_input('Enter Interface : ')
address = raw_input('Enter IP Address : ')
netmask = raw_input('Enter Subnetmask : ')


time.sleep(1)

console.write("enable\n")
console.write("conf t\n")
console.write("username {0} privil 15 password {1}".format(username, password))
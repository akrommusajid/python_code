babnscoconimport serial
import time
import getpass

console = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 9600,
	parity = 'N',
	stopbits = 1,
	bytesize = 8,
	timeout = 8
	)

console.isOpen()
print "connection is open"
time.sleep(1)
print "\nplease restart your router\n\n"
time.sleep(1)

while True:
	if console.inWaiting() == 1:
		print "recovery password is starting"
	if console.inWaiting() > 0:
		time.sleep(1)
		read_data = console.read(console.inWaiting())
		if '####' in read_data:
			print '\n\n\n\nentering rommon mode'
			time.sleep(1)
			console.sendBreak()
			break

time.sleep(1)
console.write("confreg 0x2142\nreset\n")

while True:
	if console.inWaiting() > 0:
		time.sleep(1)
		read_data = console.read(console.inWaiting())
		if "Would you like" in read_data:
			console.write("no\n")
			break

time.sleep(1)
console.write("\r\n\r\n\r\n")
console.write("enable\ncopy startup running\n\n")
username = raw_input("Enter your new username : ")
password = getpass.getpass("Enter your new password : ")
time.sleep(1)
console.write("conf t\n")
console.write("username {0} privilege 15 password {1}\n".format(username, password))
console.write("config-register 0x2102\n")
console.write("end\nwrite\n\n")
time.sleep(1)
print "\n\nYour router was succeed to recovery"
reboot = raw_input("Do you want to reboot the router?[yes/no]: ")
time.sleep(1)

if "yes" or "y" in reboot:
	console.write("reload\n\n\n")
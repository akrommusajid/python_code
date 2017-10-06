import serial
import sys
import time
import credentials

def main():
	console = serial.Serial(
		port = '/dev/ttyUSB0',
		baudrate = 9600,
		parity='N',
		stopbits=1,
		bytesize=8,
		timeout=8
	)

	if not console.isOpen():
		sys.exit()

	console.write('enable\r\n')
	time.sleep(1)
	input = console.read(console.inWaiting())
	if 'Password' in input:
		console.write('cisco' + '\r\n')
		time.sleep(1)
	
	console.write('show ip int brief\r\n')
	time.sleep(1)
	input = console.read(console.inWaiting())
	
	print input

main()
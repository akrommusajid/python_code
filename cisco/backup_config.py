import paramiko
import time

def disable_paging(conn):
	'''Disable pagin on Cisc Router'''
	conn.send("terminal length 0\n")
	time.sleep(1)

	output=conn.recv(1000)

	return output

if __name__ == '__main__':

	address='192.168.0.102'
	username='cisco'
	password='cisco'
	en_pass='cisco'

	conn_pre=paramiko.SSHClient()

	conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	conn_pre.connect(address, username=username, password=password, look_for_keys=False, allow_agent=False)

	print '*******************************************'
	print 'SSH Connection Establishd to %s' % address

	conn = conn_pre.invoke_shell()

	print 'SSH session established'

	output = conn.recv(1000)

	print output

	disable_paging(conn)

	conn.send('\n')
	conn.send('enable\n%s\n' % en_pass)
	conn.send('show run\n')

	time.sleep(5)

	output = conn.recv(50000000)

	print output

	time.sleep(1)

	print '*********************************************'
	print 'saving router configuration'
	print
	print

	time.sleep(3)

	with open(address, 'w') as f:
		f.write(output)
		f.close()

	conn.send('exit\n')

	time.sleep(1)

	print '*********************************************'
	print 'SSH connection closed from %s' % address
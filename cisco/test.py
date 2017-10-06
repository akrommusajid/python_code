import StringIO
import paramiko
import time

addresses = ['192.168.0.55','192.168.0.100']
username = 'cisco'
password = 'cisco'
secret = 'cisco'


for addr in addresses:

	sshclient = paramiko.SSHClient()
	sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	sshclient.connect(addr, username=username, password=password, look_for_keys=False, allow_agent=False)

	conn = sshclient.invoke_shell()
	print conn.recv(1000)

	conn.send('show ip int brief\n')
	time.sleep(1)
	output = conn.recv(10000)

	lines = StringIO.StringIO(output)
	
	for line in lines:
		print line
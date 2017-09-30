import paramiko
import time
import textfsm
from openpyxl import Workbook

def disable_paging(conn):
	'''Disable pagin on Cisc Router'''
	conn.send("terminal length 0\n")
	time.sleep(1)

	output=conn.recv(1000)

	return output

if __name__ == '__main__':

	open_file = open('hosts')
	addresses = open_file.readlines()

	book = Workbook()
	sheet = book.active

	header = [['Hostname','Interface','Address','status','protocol']]
	
	for s in header:
	 	sheet.append(s)
	
	for address in addresses:

		username = 'cisco'
		password = 'cisco'
		en_pass = 'cisco'

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
		conn.send('show ip int br\n')
		time.sleep(3)
	
		output = conn.recv(1000000)
	
		print '**************************************'
		print 'Terminate SSH Connection        '
		print '**************************************'
		conn.send('exit\n')
		time.sleep(1)
	
		print '**************************************'
		print 'displaying raw data         '
		print '**************************************'
		raw_data = output
		template = open('interfacebrief.textfsm')
		table = textfsm.TextFSM(template)
		fsm_results = table.ParseText(raw_data)
	
		print fsm_results
		
		for s in fsm_results:
			sheet.append(s)
	
        print '**************************************'
        print 'Saving to Spreadsheet'
        print '**************************************'
	
        time.sleep(2)
	#save file in xlsx
	book.save('interface brief.xlsx')
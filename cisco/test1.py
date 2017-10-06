import re
from napalm import get_network_driver
import time


file = open('data.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
	splitted = line.split()
	address = splitted[0]
	username = splitted[1]
	password = splitted[2]
	config = splitted[3]
	driver = splitted[4]

	print address
	print username
	print password
	print config
	print driver

	driver = get_network_driver(driver)
	router = driver(address, username, password)
	router.open()
	router.load_merge_candidate(filename=config)

	compare = router.compare_config()

	print compare
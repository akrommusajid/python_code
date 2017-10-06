import re

regex = r'\w+ \d+'
matches = re.findall(regex, "akrom 1993, arum 1993, ajid 1993")
for match in matches:
	print("Full Match : %s" % (match))

regex = r'(\w+) \d+'
matches = re.findall(regex, "Januari 14, Maret 14, April 18")
for match in matches:
	print("Match mounth : %s" %(match))

regex = r'\w+ (\d+)'
matches = re.findall(regex, "Januari 14, Maret 14, April 18")
for match in matches:
	print("Match number : %s" % (match))
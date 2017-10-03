import re

regex = r'([a-zA-Z]+) (\d+)'
if re.search(regex, "akrommusajid 1993"):
	match = re.search(regex, "akrommusajid 1993")
	print(match.start())
	print(match.end())
	
	print("Full match : %s" % (match.group(0)))

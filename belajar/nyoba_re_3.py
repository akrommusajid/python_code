import re

regex = re.compile(r'\w+ \d+')
result = regex.search("agustus 17, mei 18, juni 19")
if result:
	print("Search result from %s to %s" % (result.start(), result.end()))
	print("Search result : %s" % (result.group()))

for result in regex.findall("agustus 17, mei 18, juni 19"):
	print("Full match : %s" % (result))
# Add up the number of creatures in a data file
total = 0
reader = open('dmitri-2014.txt', 'r')
for line in reader:
	if line.startswith('#'):
		pass
	elif line.startswith('Date'):
		pass
	else:
		temp = line.strip()
		fields = temp.split(',')
		count = int(fields[2])
		total = total + count
reader.close()
print('total number of creatures seen', total)

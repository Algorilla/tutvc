# Add up the number of creatures in a data file
import sys

all_filenames = sys.argv[1:]
total = 0
for filename in all_filenames:
	reader = open(filename, 'r')
	for line in reader:
		if line.startswith('#') or line.startswith('Date'):
			pass
		else:
			temp = line.strip()
			fields = temp.split(',')
			count = int(fields[2])
			total = total + count
	reader.close()
print('total number of creatures seen', total)

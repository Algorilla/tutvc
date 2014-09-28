""" Add up the number of creatures in  a data file """
import sys

def get_count(line):
    """Extracts the count porition of a data record and returns a number"""
    temp = line.strip()
    fields = temp.split(',')
    count = int(fields[2])
    return count

def should_skip_line(line):
    """Skips line if a comment or data title"""
    return line.startswith('#') or line.startswith('Date')

def get_total(source):
    """Count the total number of creatures in  a data file"""
    total = 0
    for line in reader:
        if should_skip_line(line):
            pass
        else:
            total = total + get_count(line)
    return total

all_filenames = sys.argv[1:]
for filename in all_filenames:
    reader = open(filename, 'r')
    total = get_total(reader)
    reader.close()
    print('total number of creatures seen:', total)

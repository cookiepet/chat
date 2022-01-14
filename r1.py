# read file
def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding='utf-8-sig') as f: # 'utf-8-sig will remove coding information at begining.'
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None # Default value for person. None value for person.
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person: # if person have value, will run this code.
			new.append(person + ': ' + line)

	return new
	# print(new)

def write_file(file_name, lines):
	with open(file_name, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	# print(lines)
	write_file('output.txt', lines)

main()
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
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_picture_count = 0
	viki_picture_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
		#print(s)
	print('Allen says:', allen_word_count)
	print('Allen stick:', allen_sticker_count)
	print('Allen sends picture:', allen_picture_count)
	print('Viki says:', viki_word_count )
	print('Viki stick:', viki_sticker_count)
	print('Viki sends picture:',  viki_picture_count)

	return new
	# print(new)

def write_file(file_name, lines):
	with open(file_name, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# print(lines)
	#write_file('output.txt', lines)

main()
# Seperate words which don't have mark.

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip()) # .strip can remove \n

for line in lines:
	s = line.split(' ')
	time = s[0][:5] # Strip can be considered as array.
	name = s[0][5:]
	print(time, name)

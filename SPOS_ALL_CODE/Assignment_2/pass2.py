from pass1 import SYMBOL_TABLE
 
with open(".output1.txt", 'r') as inp, open("output.txt", 'w+') as out:
	for line in inp:
		line = line.strip('\n').split('\t')
		a = []
		for word in line:
			if word == '':
				continue
			if word[0] == 'S':
				idx = int(word[1:])-2
				a.append(SYMBOL_TABLE[1][idx])
			else:
				a.append(word)

		print(*a,sep='\t',file = out)

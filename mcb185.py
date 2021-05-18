def gc(dna):
	g = dna.count('G')
	c = dna.count('C')
	return (g+c)/len(dna)

def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

#orf =open reading frame
def orf(seq):
	#look for ATG
	length = []
	for i in range(len(seq) - 2):
		start = None 
		stop  = None	
		if seq[i:i+3] == 'ATG':
			start = i
	#FInd start and stop codon found read every triplets between the start and stop
			for j in range(i, len(seq) -2, 3):
				codon= seq[j: j + 3]
				if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
					stop = j 
					break 
		if stop != None: length.append((stop - start)/3)
	return length

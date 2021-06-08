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

#orf =open reading frame, print out numeric length
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

#Translate dictionary of mRNA to aa
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

def translate(seq):
	seq = seq.upper() #insure sequence in uppercase
	protein = ''
	for i in range(0, len(seq) -2, 3):
		#protein += gcode[seq[i:i+3]]
		codon = seq[i:i+3]
		#aa = gcode[codon]
		#protein += aa
		if codon in gcode:
			protein += gcode[codon]
		else:
			protein += 'x'
	return protein 
#reverse complement 
def anti(seq):
	revcomp = ''
	for i in range(len(seq)-1, -1, -1):
		nt = seq[i]
		if   nt == 'A': nt +='T'
		elif nt == 'T': nt +='A'
		elif nt == 'C': nt +='G'
		elif nt == 'G': nt +='C'
		else          : nt = 'N'
		revcomp +=nt
	return revcomp 

#print open reading frame of seq
def longest_seq(seq):
	longest_seq= ''
	max_seq    = ''
	for i in range(len(seq) - 2):
		start = None
		stop  = None
		if seq[i:i +3] == 'ATG':
			start = i
			for j in range(i, len(seq) -2, 3):
				codon =  seq[j:j+3]
				if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
					stop = j
					break
		if stop != None: longest_seq = seq[start:stop]
		if len(longest_seq) > len(max_seq): max_seq = longest_seq			
	return max_seq



	

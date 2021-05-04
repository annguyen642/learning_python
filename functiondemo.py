import random

def atseq(length, at)
	assert(length > 0)
	assert(at >= 0 and at <= 1)
	seq = [] #empty sequance
	for i in range(length):
		if random.random() < at: #generate a random number, if number is less than 0.5 chose either a or t
			seq.append(random.choice('AT')) 
		else:
			seq.append(random.choice('CG'))

	return "".join(seq) 

def composition(dna):
	a = dna.count('A') / len(dna)
	c = dna.count('C') / len(dna)
	g = dna.count('G') / len(dna)
	t = dna.count('T') / len(dna)
	return a, c, g, t

w = 11
for i in range(100):
	s = atseq(100, 0.9) # return a 100 nt sequence with 90% if them being at 
	print(s)
	for j in range(0, len(s) - w + 1):
		ss = s[j:j+w]
		print(j, ss, composition(ss))

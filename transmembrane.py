#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

#define the hydrophobic residues
def kd(seq):
	kd_count = 0
	for i in range(len(seq)):
		if   seq[i] == 'I': kd_count += 4.5
		elif seq[i] == 'V': kd_count += 4.2
		elif seq[i] == 'L': kd_count += 3.8
		elif seq[i] == 'F': kd_count += 2.8
		elif seq[i] == 'C': kd_count += 2.5
		elif seq[i] == 'M': kd_count += 1.9
		elif seq[i] == 'A': kd_count += 1.8
		elif seq[i] == 'G': kd_count -= 0.4
		elif seq[i] == 'T': kd_count -= 0.7
		elif seq[i] == 'S': kd_count -= 0.8
		elif seq[i] == 'W': kd_count -= 0.9
		elif seq[i] == 'Y': kd_count -= 1.3
		elif seq[i] == 'P': kd_count -= 1.6
		elif seq[i] == 'H': kd_count -= 3.2
		elif seq[i] == 'E': kd_count -= 3.5
		elif seq[i] == 'Q': kd_count -= 3.5
		elif seq[i] == 'D': kd_count -= 3.5
		elif seq[i] == 'N': kd_count -= 3.5
		elif seq[i] == 'K': kd_count -= 3.9
		elif seq[i] == 'R': kd_count -= 4.5
	return kd_count/len(seq)

#identify sequences with Proline to later find sequence with no P in them 
def contain_P(seq):
	for aa in seq:
		if aa == 'P': return True
	return False

#Set window size and conditions 
# hnp = hydrophobic no proline
def hnp(seq, w, t):
	for i in range (len(seq) - w + 1):
		win = seq[i:i+w]
		if kd(win) >= t and not contain_P(win): return True 
	return False	
				
#get all of the seqences
ids = []
proteins = []
with open(sys.argv[1]) as fp:
	seq = []
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			words = line.split()
			ids.append(words[0][1:]) 
			if len(seq) > 0 : proteins.append(''.join(seq))
			seq = []
		else:
			seq.append(line)
	proteins.append(''.join(seq))
#look for hydrophobic residue and print out id of seq with transmembrane
w_signal   = 8
w_transmem = 11
t_signal   = 2.5
t_transmem = 2.0
kd_count   = 0

#Print out the id of transmembrane proteins 
for id,seq in zip(ids,proteins):
	nterm = seq[:30]
	cterm = seq[30:]
	if hnp(nterm, w_signal, t_signal) and hnp(cterm, w_transmem, t_transmem):
		print(id)	
	
		


	

	
"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""

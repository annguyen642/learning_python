#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_length = int(sys.argv[3])

genome= [0]*genome_size
for i in range(read_num): #create empty genome with the genome size.Fill genome with reads and repeat, counts all of the reads	
	k=random.randint(0, genome_size - read_length)
	for j in range(read_length):
		genome[j+k] +=1
#print(genome)

#find the min, max, avg number of reads
min= genome[read_length]
max= genome[read_length]
read = 0
for v in genome[read_length:-read_length]: #sampling genome starting at the first 100 and last 100 (100 is the read_length)
	if v < min: min=v
	if v > max: max=v
	read+=v
mean = read/(genome_size - 2*read_length) #avg is adding up the reads over the coverage of the genome excluding both ends
print(min, max,f'{mean:.5f}')





"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""

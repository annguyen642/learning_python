#!/usr/bin/env python3

import argparse
import mcb185
import random 

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

parser = argparse.ArgumentParser(description='Explore open reading frame.')

# optional arguments with default parameters
parser.add_argument('--size', required=False, type=int, default=4500000,
	metavar='<str>', help='genome size [%(default)1]')
parser.add_argument('--orfmin', required=False, type=int, default=100,
	metavar='<int>', help='minium open reading frame [%(default)i]')
parser.add_argument('--gc', required=False, type=float, default=0.5,
	metavar='<float>', help='gc_fraction [%(default).3f]')

#switches 
parser.add_argument('--info', action='store_true',
	help='provide additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')

# finalization
arg = parser.parse_args()

#Program run random num generator and everytime will give the samee random num
if arg.seed: random.seed(1)

if arg.info: print(arg.size, arg.orfmin, arg.gc)

#generate random genome of specified size, GC composition 
seq = mcb185.randseq(arg.size, arg.gc)
#print(seq)

#version1 of orfogram using imported mcb185 lib
frame= mcb185.orf(seq)

hist = [0]*int((max(frame) + 1))

for i in frame:
	hist[int(i)] += 1

for j in range(len(hist)):
	print("length of orf:", int(j), "freq:", hist[int(j)])

"""
"""
#version2 of orfogram w/o importing from mcb185 lib
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
count = 0
for n in length:
	if n>arg.orfmin:
		count += 1
#print(count)

#Print empyty and fill empty histogram
hist = [0]*(int(max(length))+ 1)
for i in length:
	hist[int(i)] += 1 
#print hist
for j in range(len(hist)):
	#if hist[j] != 0:
		print("orf length:", j, "freq:", hist[j])
	#print(length)	
"""

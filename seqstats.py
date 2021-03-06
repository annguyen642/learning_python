#!/usr/bin/env python3

import argparse
import mcb185
import statistics

parser = argparse.ArgumentParser(description='stats about sequence.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required fasta file')
arg = parser.parse_args()

length = []
for name in seq in mcb185.read_fasta(arg.file):
	#print(name,len(seq))
	length.append(len(seq))

length.sort()
#print(length)

#Min and max
print('min is', min(length))
print('max is', max(length))

#sum = 0
#for value in length:
	#sum += value
print('sum is', sum(length))

#mean, median, and n50
print('mean is', statistic.mean(length))
print('median is', statistic.median(length))
print('n 50 is', mcb185.n50(len))

#print(length)

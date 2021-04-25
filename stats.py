#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

p = []
for s in sys.argv[1:]:
	p.append(float(s))
print(p)

txt = 'Count'
count = 0
for i in range (len(p)):
	count += 1	
print(f'{txt}:{i+1}')

p.sort()
txt = 'Minium'
first = p[0]
print(f'{txt}: {first}')
txt = 'Maxium'
last = p[i]
print(f'{txt}: {last}')

txt = 'Mean'
mean= 0
for i in range(len(p)):
	mean += p[i]/len(p)
print(f'{txt}: {mean:.3f}')

txt = 'Std.dev'
stdev = 0 
sum = 0 
for i in range(len(p)):
	sum += (p[i]- mean)**2
	stdev = math.sqrt((sum)/(len(p)))
print(f'{txt}: {stdev:.3f}')

txt = 'Median'
if len(p) % 2 == 0: 
	med_1= len(p)//2 
	med_2= len(p)//2 -1
	med= (p[med_1] + p[med_2])/2
	print(f'{txt}: {med:.3f}')
else:
	med= len(p)//2
	print(f'{txt}:{p[med]:.3f}')



	







"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""

#!/usr/bin/env python3

# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

aa= 'ACDEFGHIKLMNPQRSTVWY'
count = 0
for i in range(len(aa)):
	for j in range(i +1, len(aa)):
		count += 1
		print(aa[i],aa[j])
print(count)

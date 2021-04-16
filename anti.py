#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
anti = ''
for i in range(len(dna) -1, -1, -1):
    nt = dna[i]
    if   nt == 'A': anti += 'T'
    elif nt == 'T': anti += 'A'
    elif nt == 'C': anti += 'G'
    elif nt == 'G': anti += 'C'  
print(anti)
   
"""
python3 anti.py
TTTTTTTTTTTCAGT
"""

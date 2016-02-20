#!/usr/bin/env python

"""
Name: Randomly samples sequences 

Author: Madhvi Venkatraman
Date: November 13th, 2014

Randomly sample x number of sequences from a fasta file

Usage: python random_seq.py input.fasta output.fasta n
    Where n is your subsample number

Example: python random_seq.py A15F.fasta A15F_subsample.fasta 100

Notes: Requires Python 2.7 and Biopython (www.biopython.org)

"""

import random
import argparse
from Bio import SeqIO

def parse_args():
    parser = argparse.ArgumentParser(description="Randomly sample x number of sequences from a fasta file")
    parser.add_argument("input_fasta", type= str, help = "The input file in fasta format")
    parser.add_argument("output_fasta", type= str, help = "The output file in fasta format")
    parser.add_argument("sample_no", type= int, help = "The number of sequences you want to sample as an integer")
    return parser.parse_args()

# Generates n random numbers with your number of sequences as a range

def random_num(num, count):
    rand = list()
    if num >= count:
    	print("Your sample number is greater or equal to the number of sequences in your input file.")
    upper = count-1
    population = range(0, upper)
    rand = random.sample(population, num)
    return rand

# Gets the sequences ids and sequences for these random numbers

def get_seq(rand, fastafile):
    sub = ""
    subsample = ""
    for r in rand:
        seqid = fastafile[r].id
        seq = fastafile[r].seq  
        sub = ">" + str(seqid) + "\n" + str(seq) + "\n"
        subsample = subsample + sub
    return subsample

def main():
    args = parse_args()
    infasta = open("{0}".format(args.input_fasta), 'rU')
    outfasta = open("{0}".format(args.output_fasta), 'w')
    num = args.sample_no
    count = SeqIO.convert(infasta, "fasta" , "input.txt", "tab")
    infasta.close()
    infasta2 = open("{0}".format(args.input_fasta), 'rU')
    fastafile = list(SeqIO.parse(infasta2, "fasta"))
    rand = random_num(num, count)
    subsample = get_seq(rand, fastafile)
    outfasta.write(subsample)
    infasta2.close()
    outfasta.close()

if __name__ == '__main__':
    main()

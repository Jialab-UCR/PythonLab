#!/usr/bin/env python3.4

from Bio.Seq import Seq
from Bio import SeqIO
import re

def main():
    wtoc = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
    fout = open('xiaoxia_chr_strand_loci_allele.txt', 'wt')
    for seq_record in SeqIO.parse('HSGRCH3771_final.fa', 'fasta'):
        get_loci(seq_record.id, seq_record.seq, fout)

    fout.close()

    
def get_loci(chrid, chrseq, fout):
    with open('xiaoxia_chr_strand_loci.txt', 'rt') as f:
        for line in f:
            line = line.rstrip()
            lst = line.split()
            if lst[0]==chrid:
                if lst[1] == '1':
                    allele = chrseq[int(lst[2])-1]
                elif lst[1] == '-1':
                    allele = wtoc[chrseq[int(lst[2])-1]]
                fout.write(line+'\t'+allele+'\n')
                print (line+'\t'+allele+'\n')
                
if __name__ == '__main__':
    main()
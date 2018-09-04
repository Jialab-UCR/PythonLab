#!/usr/bin/env python3.4

from collections import OrderedDict
import os

annos = OrderedDict()

with open('Zmays_284_5b+.annotation_info.txt', 'rt') as f:
	for line in f:
		lst = line.split('\t')
		if lst[1] not in annos.keys():
			annos[lst[1]] = lst[-1]

files = os.listdir('candidate_gene')

for fl in files:
	if fl.endswith('.txt'):
		fout = open('candidate_gene_annotation/'+fl+'.annotation', 'wt')
		with open('candidate_gene/'+fl, 'rt') as f:
			for line in f:
                		line = line.strip()
                		lst = line.split('\t')
                		gene = lst[8][5:]
                		if gene in annos.keys():
                			fout.write(line+'\t'+annos[gene])

		fout.close()

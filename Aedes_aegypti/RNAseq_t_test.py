import re
import scipy
import numpy as np
from scipy import stats
from collections import OrderedDict, defaultdict


    
def norm(sam, stan):
    # get the normalization ratio
    geex, cose, coan, coto, struc, pseudo, mir = 0, 0, 0, 0, 0, 0, 0
    file = sam+'_all/sum_'+sam+'_all.txt'
    with open (file) as f:
        for line in f:
            #line = re.sub(r'\s+$', r'', line)
            line = line.rstrip()
            if re.search(r'^geex\t\S+\t\S+\t\S+', line):
                mch = re.search(r'^geex\t\S+\t\S+\t(\S+)', line) # all
                geex = float(mch.group(1))
            if (re.search(r'^protein_coding\t\S+\t\S+\t\S+', line)):
                mch = re.search(r'^protein_coding\t(\S+)\t(\S+)\t(\S+)', line)
                cose = float(mch.group(1)); coan = float(mch.group(2)); coto = float(mch.group(3))
            if (re.search(r'^struc\t\S+\t\S+\t\S+', line)):
                mch = re.search(r'^struc\t(\S+)\t\S+\t\S+', line) # sense
                struc = float(mch.group(1))            
            if (re.search(r'^pseudogene\t\S+\t\S+\t\S+', line)):
                mch = re.search(r'pseudogene\t(\S+)\t\S+\t\S+', line) # sense
                pseudo = float(mch.group(1))            
            if (re.search(r'^miRNA\t\S+\t\S+\t\S+', line)):
                mch = re.search(r'miRNA\t(\S+)\t\S+\t\S+', line) # sense
                mir = float(mch.group(1))            
            if (re.search(r'^premiRNA\t\S+\t\S+\t\S+', line)):
                mch = re.search(r'premiRNA\t(\S+)\t\S+\t\S+', line) # sense
                premir = float(mch.group(1))
            if (re.search(r'^exex', line)):
                break

    print ('''total %.2f
sense coding %.2f
anti coding %.2f
total coding %.2f
sense struc %.2f
sense pseudo %.2f
sense miRNA %.2f\n''' % (geex, cose, coan, coto, struc, pseudo, mir))
        
    if (stan == 'mir'):
        ratio = 1000000/mir
    elif (stan == 'cose'):
        ratio = 5000000/cose
    elif (stan == 'coan'):
        ratio = 2000000/coan
    elif (stan == 'coto'):
        ratio = 5000000/coto
    elif (stan == 'tot'):
        ratio = 5000000/geex
    
    print ('Normalization ratio', ratio, '\n\n')
    
    return ratio

ano = {}

with open('Aedes-aegypti-Liverpool_TRANSCRIPTS_AaegL3.3.fa', 'rt') as f:
    for line in f:
        if line.startswith('>'):
            line = line.rstrip()
            line = re.sub('>', '', line)
            lst = line.split()
            gene = lst[0].split('-')
            geneid = gene[0]+'\t'+lst[0]
            lst.pop(0)
            info = ' '.join(lst)
            ano[geneid] = info

coding = OrderedDict(defaultdict(list))

stan = 'cose'

ctrl = '032816ctrl'
treat = '032816LC506hr'


wt = input('WT samples seperated with comma (3 replicates):')
wt = wt.rstrip()
mut = input('Mutant samples seperated with comma (3 replicates):')
mut = mut.rstrip()

samples = re.split(r'\s*\,+\s*', wt) + re.split(r'\s*\,+\s*', mut)

for sam in samples:
    ra = norm(sam, stan)
    in_file = sam+'_all/sum_'+sam+'_all_17_cdna_protein_coding.txt'
    with open(in_file, 'rt') as f:
        for line in f:
            line = line.rstrip()
            lst = line.split()
            gene = lst[0]+'\t'+lst[1]
            if gene not in coding.keys():
                coding[gene] = []
            coding[gene].append(float(lst[2])*ra)

fh1 = open('T_test_'+ctrl+'_'+treat+'_'+'005.txt', 'wt')
fh2 = open('T_test_'+ctrl+'_'+treat+'.txt', 'wt')
fh1.write('Gene\tTranscript\t')
fh2.write('Gene\tTranscript\t')

for sam in samples:
    fh1.write(sam+'\t')
    fh2.write(sam+'\t')

fh1.write('WT mean\tMUT mean\tp-value\n')
fh2.write('WT mean\tMUT mean\tp-value\n')

for k,v in coding.items():
    x = v[0:3]
    y = v[3:6]
    x_m = round(np.mean(x), 3)
    y_m = round(np.mean(y), 3)

    v1 = str(v[0])
    v2 = str(v[1])
    v3 = str(v[2])
    v4 = str(v[3])
    v5 = str(v[4])
    v6 = str(v[5])

    
    test = stats.ttest_ind(x,y, equal_var=True)
    t = round(test[0], 3)
    p = round(test[1], 3)
    if p < 0.05:
        fh1.write(k+'\t'+v1+'\t'+v2+'\t'+v3+'\t'+v4+'\t'+v5+'\t'+v6+'\t'+str(x_m)+'\t'+str(y_m)+'\t'+str(p)+'\t'+ano[k]+'\n')
    
    fh2.write(k+'\t'+v1+'\t'+v2+'\t'+v3+'\t'+v4+'\t'+v5+'\t'+v6+'\t'+str(x_m)+'\t'+str(y_m)+'\t'+str(p)+'\t'+ano[k]+'\n')
    
fh1.close()
fh2.close()



            
            

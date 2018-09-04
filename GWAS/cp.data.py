import os

start = 477997
rawdir = 'raw_seq/'
outdir = 'fastq/'

for i in range(3):
        num = start + i
        sa = i + 1
	sample = rawdir + 'ERR' + str(num)+ '*'
	

        os.system('mv ' + sample + ' ' + outdir)
        #os.system('gunzip ' + outdir + '*.gz')
	os.system('echo file' + str(sa) + ' is copied')

os.system('echo dataset is ready')

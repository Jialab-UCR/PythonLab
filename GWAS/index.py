#!/usr/bin/python

import os,sys
import time

start = 477442

outdir = 'bwa_out/'

for i in range(850):
	num = start + i
	sample = 'ERR' + str(num)
	
	sorted_out = outdir + sample + '.sorted.bam'
	
	os.system('samtools-v1.3 index ' + sorted_out)

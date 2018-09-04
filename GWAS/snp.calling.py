#!/usr/bin/python

# import subprocess as sp
import os,sys
import time

start = 477445
rawdir = 'dataset.1/'
outdir = 'bwa_out/'

for i in range(47):
	num = start + i
	sample = 'ERR' + str(num)
	seq1 = rawdir + sample + '_1.fastq'
	seq2 = rawdir + sample + '_2.fastq'
	seq = seq1 + ' ' + seq2
	bwa_out = outdir + sample + '.bam'
	sorted_out = outdir + sample + '.sorted.bam'
	localtime = time.asctime(time.localtime(time.time()))
	
	os.system('echo ' + '\*'*10 + sample + '\*'*10)
	os.system('echo start alignment at ' + localtime)
	
	### alignment and fixmate, generate a bam file
	os.system('bwa mem -t 8 -v 1 -M nipponbare7.fa ' + seq + '|'
		  'samtools1.3 fixmate -O bam - ' + bwa_out + ' && echo --------- fixmate ok ---------')	
	
	### sort, index, generate a sorted bam file and remove the old one
	os.system('samtools1.3 sort -@ 8 -T ERRtmp -O bam -o ' + sorted_out + ' ' + bwa_out
	          + ' && echo --------- sort ok --------- && rm ' + bwa_out) 
	os.system('samtools1.3 index ' + sorted_out)
	
	localtime = time.asctime(time.localtime(time.time()))
	os.system('echo alignment complete at ' + localtime)
	os.system('echo ' + '\*'*60 + ' && echo')

### snp calling
# all = outdir + 'ERR*.sorted.bam'
# os.system('samtools1.3 mpileup -guf nipponbare7.fa -q 40 ' + all + ' | bcftools1.3 call -vmO z -V indels -o ERR.nohup.snp.vcf.gz')
# os.system('rm *.sorted.*')

# localtime = time.asctime(time.localtime(time.time()))
# os.system('echo ' + localtime)
os.system('echo ' + '\*'*10 + ' ALIGNMENT IS COMPLETED ' + '\*'*10)

## base quality -Q




# datadir = 'dataset.1'
# seqfiles = os.listdir(datadir)

#program = 'ls -l'
#proc = sp.Popen( [program] )

#os.system('bowtie2 -p 8 -x wu_0 -U wu_0_A_wgs.fastq -S test.out.2.sam && echo alignment completed')

#datadir = '/usr/biobin'
#readfilenames = os.listdir(datadir)
#for file in readfilenames:
#	print file, '\n'
#os.system('ls -l dataset.1 | wc -l')

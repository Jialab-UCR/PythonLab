import subprocess as sp
from subprocess import call


alignment1 = ('tophat2 -p 8 -o tophat2_out/flowering/D330 -r 50 -i 70 --library-type fr-unstranded \
              nipponbare7 fastq/flowering/D330.read1_Clean.fq fastq/flowering/D330.read2_Clean.fq')

alignment2 = ('tophat2 -p 8 -o tophat2_out/flowering/MH63 -r 50 -i 70 --library-type fr-unstranded \
              nipponbare7 fastq/flowering/MH63.read1_Clean.fq fastq/flowering/MH63.read2_Clean.fq')

print (alignment1+'\n')
call(alignment1, shell = True)

print (alignment2+'\n')
call(alignment2, shell = True)

#rename1 = ('mv tophat2_out/flowering/D330/accepted_hits.bam tophat2_out/flowering/D330/D330.accepted_hits.bam')
#rename2 = ('mv tophat2_out/flowering/MH63/accepted_hits.bam tophat2_out/flowering/MH63/MH63.accepted_hits.bam')

#print (rename1+'\n')
#call(rename1, shell = True)

#print (rename2+'\n')
#call(rename2, shell = True)

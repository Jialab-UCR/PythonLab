#!/bin/bash -x
module load java/8

java -Xmx8g -jar beagle.14Jun16.dd3.jar nthreads=8 gt=ERR.snp.QUAL50.merged.DP8_25.miss25.recode.vcf.share.gz out=ERR.snp.QUAL50.merged.DP8_25.miss25.recode.vcf.share.impute.gt

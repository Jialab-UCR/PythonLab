from collections import OrderedDict

chr = OrderedDict()
Total = 0
with open('ERR.snp.QUAL50.merged.DP8_25.miss25.recode.vcf.share.impute.gt.vcf') as f:
	for line in f:
		line = line.rstrip()
		lst = line.split('\t')
		if lst[0].startswith('Chr'):
			if lst[0] not in chr.keys():
				chr[lst[0]] = 0
			chr[lst[0]] += 1
			Total += 1

for k, v in chr.items():
	print (k + '\t' + str(v))
print('Total'+'\t'+str(Total))

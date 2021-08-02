#!/usr/bin/env python3

import urllib
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.request as urlrq
import math
import certifi
import ssl
import sys
import numpy as np
import os
import matplotlib.pyplot as plt
from collections import OrderedDict
wd = os.getcwd()

try:
  file = sys.argv[1]
  organ = sys.argv[2]
except IndexError:
  print('\n HbCGMEx.py code requires: HbCGM output result file and name of the organ of interest for gene expression')
  pass

def barchar(file):

	global g2
	with open(file) as ij:
		g = ij.name
		g1 = g.split('/')
		g2 = g1[-1].split('.')
		lines = ij.readlines()
		line_strains = tuple(lines[1].split('\t'))
		line_values = list(lines[2].split('\t'))
		y_pos = np.arange(len(line_strains))
		# TO DO fix bars
		low = line_values[0]
		high = max(y_pos)
		plt.ylim(math.ceil(int(low)), math.ceil(high))
		plt.bar(y_pos, line_values, align='center')
		plt.xticks(y_pos, line_strains, color='black', rotation=90)
		plt.yticks(color='black')
		plt.ylabel('values')
		plt.xlabel('strains', fontweight='normal', color = 'black', fontsize='3')
		plt.title(g2[0]+" phenotype values")
		# plt.show()
		plt.savefig(g2[0]+'.png')
		print('--> phenotype values chart is done ...')

def expression(file, organ): 
	
	print("--> getting "+sys.argv[2]+ " expression values of genes with cSNPs ...")
	express = []
	with open(file) as ij:
		g = ij.name
		g1 = g.split('/')
		g2 = g1[-1].split('.')
		for i in ij.readlines()[3:]:
			i = i.rstrip().split("\t")
			if i[1] == '1' or i[1] == '2':
				try:
					response = urlrq.urlopen('https://www.ebi.ac.uk/fg/rnaseq/api/tsv/0/getExpression/mus_musculus/'+i[0], context=ssl.create_default_context(cafile=certifi.where()))
					for r in response.readlines()[1:]:
						r = r.decode('utf-8').rstrip().split('\t')
						if str(r[5]) == sys.argv[2] and round(float(r[2])) >= 35:
							express.append(i[0]+'\t'+ str(round(float(r[2]))) +'\t'+ r[5] +'\t'+ i[1]+'\t'+i[5]+'\t'+i[6]+'\t'+i[7])
				except urllib.error.URLError as q:
					print(q)
			
	try:
		cSNP = []
		print("--> working on finding cSNPs in genes expressed in " +sys.argv[2]+" ...")
		for ex in OrderedDict.fromkeys(express):
			e = ex.rstrip().split('\t')
			with open(os.path.join(wd+"/data"+'/gene_coding_snps.txt')) as gc:
				for g in gc:
					g = g.rstrip().split('\t')
					if g[2] == e[0]:
						cSNP.append(g[2]+'\t'+ g[3]+'\t'+ g[4]+'\t'+ g[5])
						with open(g2[0]+'_gene_coding_snps.txt', 'a') as k:
							k.write(g[2]+'\t'+ g[3]+'\t'+ g[4]+'\t'+ g[5]+'\n')
	except:
		pass
	
	try:
		cSNP1 = []
		print("--> working on finding functional cSNPs in genes expressed in " +sys.argv[2]+" ...")
		for cs in OrderedDict.fromkeys(cSNP):
				c = cs.rstrip().split('\t')
				with open(os.path.join(wd+"/data"+"/Functional-data.txt")) as rr:
					for r in rr:
								r = r.rstrip().split("\t")
								if r[-1] == c[0] and int(c[1]) >= int(r[2]) and int(c[1]) <= int(r[3]):
									cSNP1.append(c[0]+'\t'+ c[1]+'\t'+ r[1])
									with open(g2[0]+'_Functional-data.txt', 'a') as k:
										k.write(c[0]+'\t'+ c[1]+'\t'+ r[1]+"\n")
									#print("--> "+ c[0]+ " expressed in "+sys.argv[2] +", has " +c[1]+" mutated residue whcih is present within "+r[1]+" region")
	except:
		pass

	try:
		NGIphen = []
		print("--> working on finding mosue phenotypes of functional cSNPs in genes expressed in " +sys.argv[2]+" ...")
		for cs in OrderedDict.fromkeys(cSNP1):
			c = cs.rstrip().split('\t')
			with open(os.path.join(wd+"/data"+"/MGI_pheno_genes.txt")) as rr:
				for r in rr:
					r = r.rstrip().split("\t")
					if c[0] == r[0]:
						NGIphen.append('\t'.join(c)+"\t"+r[-1]+"\t"+r[1])
						with open(g2[0]+'_MGI_pheno_genes.txt', 'a') as k:
							k.write('\t'.join(r)+'\n')
						#print("--> "+ c[0]+ " previously reported for " +r[-1]+" in mouse")
						
	except:
		pass

	try:
		HuGwas = []
		print("--> working on finding human phenotypes of functional cSNPs in genes expressed in " +sys.argv[2]+" ...")
		for cs in OrderedDict.fromkeys(cSNP1):
			c = cs.rstrip().split('\t')
			with open(os.path.join(wd+"/data"+"/gene_disease_associations.txt")) as rr:
				for r in rr:
					r = r.rstrip().split("\t")
					if c[0] == r[0].capitalize():
							HuGwas.append('\t'.join(c)+"\t"+r[1]+"\t"+r[2] +"\t"+r[-1])
							with open(g2[0]+'_H-gene_disease_associations.txt', 'a') as k:
								k.write('\t'.join(c)+"\t"+r[-1]+"\t"+r[1]+'\n')
							#print("--> "+ c[0]+ " previously reported for " +r[-1]+" in human GWAS")
		
	except:
		pass
	
	print("--> "+ "pipeline is finished and probably successful.")

def HbCGM(file, organ):

	#barchar(sys.argv[1])

	expression(sys.argv[1], sys.argv[2])


if __name__=='__main__':

    try:
    	
    	HbCGM(sys.argv[1], sys.argv[2])
	
    except NameError:
	    pass

#To Run
#pytohn HbCGMEx.py <HbCGM results file> <organ of interest> 

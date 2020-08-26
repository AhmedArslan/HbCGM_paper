#!/usr/bin/env python3

import urllib
from urllib.request import urlopen
from urllib.error import HTTPError
import math
import sys
import numpy as np
import matplotlib.pyplot as plt

try:
  file = sys.argv[1]
  organ = sys.argv[2]
except IndexError:
  print('\n HbCGMEx.py code requires: HbCGM output result file and name of the organ of interest for gene expression')
  pass

def barchar(file):

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
		print('phenotype values chart is done ...')

def expression(file, organ): 
	
	print("printing expression values of genes with cSNPs ...")
	express = []
	with open(file) as ij:
		g = ij.name
		g1 = g.split('/')
		g2 = g1[-1].split('.')
		for i in ij.readlines()[3:]:
			i = i.rstrip().split()
			if i[1] == '1' or i[1] == '2':
				try:
					response = urlopen('https://www.ebi.ac.uk/fg/rnaseq/api/tsv/2/getExpression/mus_musculus/'+i[0])
					for r in response.readlines()[1:]:
						r = r.decode('utf-8').rstrip().split('\t')
						if str(r[5]) == sys.argv[2] and round(float(r[2])) >= 35:
							# print(i[0] +" expression found the organ of interest")
							express.append(i[0]+'\t'+ str(round(float(r[2]))) +'\t'+ r[5] +'\t'+ i[1])
				except urllib.error.URLError as q:
					print(q)
				
	print("printing expression values of genes with cSNPs is done")
	
def HbCGM(file, organ):

	barchar(sys.argv[1])

	expression(sys.argv[1], sys.argv[2])

if __name__=='__main__':

    try:
    	
    	HbCGM(sys.argv[1], sys.argv[2])
	
    except NameError:
	    pass
#To Run
#pytohn HbCGMEx.py <HbCGM results file> <organ of interest> 

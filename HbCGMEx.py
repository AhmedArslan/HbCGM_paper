#!/usr/bin/env python3

import urllib
from urllib.request import urlopen
from urllib.error import HTTPError
import math
import sys

def expression(file1): 
	
	express = []
	with open(file1,'rU') as ij:
		g = ij.name
		g1 = g.split('/')
		g2 = g1[-1].split('.')
		for i in ij.readlines()[3:]:
			i = i.rstrip().split('\t')
			if i[0] == '1' or i[0] == '2':
				try:
					response = urlopen('https://www.ebi.ac.uk/fg/rnaseq/api/tsv/2/getExpression/mus_musculus/'+i[0])
					for r in response.readlines()[1:]:
						r = r.decode('utf-8').rstrip().split('\t')
						if str(r[5]) == 'brain' and round(float(r[2])) >= 35:
				except urllib.error.URLError as q:
					express.append(i[0]+'\t'+ str(round(float(r[2]))) +'\t'+ r[5])
	
	with open(g2[0]+"_expression.txt", 'a') as k:
		for e in express:
			k.write(e+"\n")

if __name__=='__main__':
	
	#to run
	# file1 = HbCGM output file
	expression(file1)



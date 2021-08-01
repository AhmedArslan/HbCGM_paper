# HbCGM_paper

The codes used to process the haplotype based computational genetic mapping output files and reported in *Arslan et al. "High Throughput Computational Mouse Genetic Analysis" bioRxiv 2020* paper

1 - HbCGM results

The result files from HbCGM for all the analyzed phenotypes can be downloaded from the following [link](https://drive.google.com/drive/folders/1HOI16TXqepgct3RTlt71AZjQ1njwuOAo?usp=sharing):

2 - HbCGMEx.py

This code takes a typical results file and organ of interest as input. and output files, contains genes with coding SNPs (cSNPs) and expression values (TRM) in the organ of interest and known biomedical phenotypes. 

  To run the code:
  
    python3 HbCGMEx.py <HbCGM file> <organ name> e.g. python3 HbCGMEx.py 50243-succinylcarnitine-M-mutation-resul.txt liver
    
  Expected output:
    
    1 - File contains all the genes with snps present in their coding or splicing regions and has expression in an organ as specified by a user.(_gene_coding_snps.txt) 
    2 - Second file contains, snps fron step (1) if they overlap with functional protein region like domain or PTM site (_Functional-data.txt).
    3 - Genes with snps that could impact protein fucntional or regulatory regions and expressed in the organ of interest are subjected to automated literature review on the gene-term association with data extracted from [phenolyzer](https://github.com/WGLab/phenolyzer), [Disgenet](https://www.disgenet.org/search) and [MGI](http://www.informatics.jax.org/), [GWAS Catalog] (https://www.ebi.ac.uk/gwas/) with default settings. 
 

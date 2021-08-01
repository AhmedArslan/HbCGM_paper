# HbCGM_paper

The codes used to process the haplotype based computational genetic mapping output files and reported in *Arslan et al. "High Throughput Computational Mouse Genetic Analysis" bioRxiv 2020* paper

1 - HbCGM results

The result files from HbCGM for all the analyzed phenotypes can be downloaded from the following [link](https://drive.google.com/drive/folders/1HOI16TXqepgct3RTlt71AZjQ1njwuOAo?usp=sharing):

2 - HbCGMEx.py

This code takes a typical results file and organ of interest as input and automate for users to reproduce he output files, contains genes with coding SNPs (cSNPs) and expression values (TRM) in the organ of interest and known biomedical phenotypes. 

  download the git:
  
    clone git https://github.com/AhmedArslan/HbCGM_paper
    
    cd HbCGM_paper

  To run the code:
  
    python3 HbCGMEx.py <HbCGM file> <organ name> e.g. python3 HbCGMEx.py 50243-succinylcarnitine-M-mutation-resul.txt liver
    
  Expected output:
    
    1 - File contains all the genes with snps present in their coding or splicing regions and has expression in an organ as specified by a user.(_gene_coding_snps.txt) 
    2 - Second file contains, snps fron step (1) if they overlap with functional protein region like domain or PTM site (_Functional-data.txt).
    3 - Genes with snps that could impact protein fucntional or regulatory regions and expressed in the organ of interest are subjected to automated literature review on the gene-term association data.
    4 - bar of phenotype values from HbCGM file
    
Data source:

Functional Protein regions:
UniProt, PTMdb, Ensembl-db

Gene-term association:

[phenolyzer](https://github.com/WGLab/phenolyzer), [Disgenet](https://www.disgenet.org/search), [MGI](http://www.informatics.jax.org/) and [GWAS Catalog](https://www.ebi.ac.uk/gwas/) with default settings. 

(see artile for all the information of data sources)

Contact::

<aarslan@stanford.edu>

# HbCGM_paper

The codes used to process the haplotype based computational genetic mapping output files and reported in *Arslan et al. "High Throughput Computational Mouse Genetic Analysis" bioRxiv 2020* paper

1 - HbCGM results

The result files from HbCGM for all the analyzed phenotypes can be downloaded from the following [link](https://drive.google.com/file/d/1ryL_R0__DKN4a_414BS1uCS2-S5bwCtC/view):

2 - HbCGMEx.py

This code takes a typical results file and organ of interest as input and automate for users to reproduce he output files, contains genes with coding SNPs (cSNPs) and expression values (TRM) in the organ of interest and known biomedical phenotypes. 

  requirements: 
  
    python (2.7 or 3.x) 
  
    The code was optmised on Mac system.
  
  
  download the git:
  
    git clone https://github.com/AhmedArslan/HbCGM_paper
    
    cd HbCGM_paper

  To run the code:
  
    python3 HbCGMEx.py <HbCGM file> <organ name> e.g. python3 HbCGMEx.py 50243-succinylcarnitine-M-mutation-resul.txt liver
    
  expected output:
  
    1 - bar of phenotype values from HbCGM file
    
    2 - File contains all the genes with snps present in their coding or splicing regions and has expression in an organ as specified by a user.(_gene_coding_snps.txt) 
    3 - Second file contains, snps fron step (1) if they overlap with functional protein region like domain or PTM site (_Functional-data.txt).
    4 - Genes with snps that could impact protein fucntional or regulatory regions and expressed in the organ of interest are subjected to automated literature review on the gene-term association data. 
    
    The file from step (4) contains the final outcome of the pipeline and information present in this file was used to validate the gene Lactb as causative agent of elevated levels of succinylcarnitine metabolies in FVB and AJ strains, see paper for more information. 
 
    
data source:

  functional Protein regions:
    UniProt, PTMdb, Ensembl-db

  gene-term association:

   [phenolyzer](https://github.com/WGLab/phenolyzer), [Disgenet](https://www.disgenet.org/search), [MGI](http://www.informatics.jax.org/) and [GWAS Catalog](https://www.ebi.ac.uk/gwas/) with default settings. 

(see artile for all the information of data sources)

contact:

<aarslan@stanford.edu>

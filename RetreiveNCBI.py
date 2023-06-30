from Bio import Entrez
from Bio.Align.Applications import ClustalOmegaCommandline 
Entrez.email = "shn_yns@eyahoo.com"
searchterm = "(\"autophagy related protein 8\"[All Fields] OR \"(ATG8)\"[All Fields] ) AND (plants[filter] AND biomol_mrna[PROP] AND refseq[filter])"
searchResultHandle = Entrez.esearch(db="nucleotide", term=searchterm, retmax=6000)
searchResult = Entrez.read(searchResultHandle)
print(searchResult)
ids = searchResult["IdList"]
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
record = handle.read()
out_handle = open('ATG8ALLplantsNCBI.fasta', 'w')
out_handle.write(record.rstrip('\n'))
in_file = "myfasta.fasta"
out_file = "atg2.sto"
clustalomega_cline = ClustalOmegaCommandline(infile = in_file, outfile = out_file, outfmt = 'stockholm', verbose = True, auto = True)
clustalomega_cline()
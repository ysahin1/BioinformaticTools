from Bio import SeqIO
import re
import csv

anno_dic = {}
with open("AllplantsATGs.fasta", "r") as handle:
    for record in SeqIO.parse(handle, 'fasta'):
        anno_dic[record.id] = record.description
locusID = []
geneID = []
protein = []
for entry in anno_dic:
    locusID.append(entry)
    annos = anno_dic[entry].split()
    if re.search('\[gene=', annos[1]):
        anno = annos[1].lstrip("[gene=")
        anno = anno.rstrip("]")
        geneID.append(anno)
    else:
        geneID.append('NA')
    if re.search('\[protein=', annos[3]):
        annop = annos[3].lstrip("[protein=")
        annop = annop.rstrip("]")
        protein.append(annop)
    else:
        geneID.append('NA')

intlist= zip(geneID, locusID, protein)
with open('ATG_NCBIIDsAndSymbols.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(intlist)    
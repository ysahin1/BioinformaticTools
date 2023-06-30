import subprocess
from Bio import SearchIO
import csv
hit_id = []
hit_evalue = []
hit_desc = []
hit_bias=[]
hit_bitscore=[]
with open("6AAlignmentResults.txt", "r") as f:
    for qresult in SearchIO.parse(f, 'hmmer3-text'):
        query_id = qresult.id  #sequence ID from fasta
        query_len = qresult.seq_len
        hits = qresult.hits
        num_hits = len(hits)
        if num_hits > 0:
            for i in range(0,num_hits):
                hit_id.append(hits[i].id)
                hit_evalue.append(hits[i].evalue) #evalue
                hit_desc.append(hits[i].description)
                hit_bias.append(hits[i].bias)
                hit_bitscore.append(hits[i].bitscore)

intlist=zip(hit_id, hit_evalue, hit_bias, hit_bitscore,hit_desc, )
with open('6dhmmerParseRes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(intlist)   
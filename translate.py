from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
input_file = "AutophagyAllplantsmRNAs.fasta"
output_file = "AutophagyAllplantsPep.fasta"
output_handle = open(output_file, "w")
for nuc_record in list(SeqIO.parse(input_file, "fasta")):

        frame_1 = SeqRecord(seq = nuc_record.seq.translate(stop_symbol=""), \
                        id = nuc_record.id + "_frame-1", \
                        description = "-")
        print (frame_1.id)
        frame_2 = SeqRecord(seq = nuc_record[1:].seq.translate(stop_symbol=""), \
                        id = nuc_record.id + "_frame-2", \
                        description = "-2")
        print (frame_2.id)
        frame_3 = SeqRecord(seq = nuc_record[2:].seq.translate(stop_symbol=""), \
                        id = nuc_record.id + "_frame-3", \
                        description = "-3")
        print (frame_3.id)
        frame_4_R = SeqRecord(seq = nuc_record.seq.reverse_complement(), \
                        id = nuc_record.id + "_frame-1-R", \
                        description = "-R1")
        frame_1_R = SeqRecord(seq = frame_4_R.seq.translate(stop_symbol=""), \
                        id = nuc_record.id + "_frame-1-R", \
                        description = "-R")
        print (frame_1_R.id)
        frame_2_R = SeqRecord(seq = frame_4_R[1:].seq.translate(stop_symbol=""), \
                        id = nuc_record.id + "_frame-2-R", \
                        description = "-R2")
        print (frame_2_R.id)
        frame_3_R = SeqRecord(seq = frame_4_R[2:].seq.translate(stop_symbol=""), \
                        id = nuc_record.id + "_frame-3-R", \
                        description = "-R3")
        print (frame_3_R.id)
        list =[frame_1, frame_2, frame_3, frame_1_R, frame_2_R, frame_3_R]
        SeqIO.write(list, output_handle, "fasta")
output_handle.close()

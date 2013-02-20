def tuples_from_FASTA_file(filename):
	"""Given a path to a FASTA file, returns a list of tuples of (id, sequence) pairs. The file
	must end in a newline character; otherwise the last sequence will be missed!"""
	try:
		f = open(filename, "r")
	except IOError:
		print "A file does not exist at this location, or some other I/O error occurred."
		return ""
	fastaList = []
	sequence_id = 0
	seq = ""
	for line in f:
		if(line[0] == ">"):
			if(sequence_id != 0):
				fastaList.append((sequence_id, seq))
			sequence_id = line[1:-1]
			seq = ""
		else:
			seq += line[:-1]
	fastaList.append((sequence_id, seq)) # last id:sequence pair, hanging around
	return fastaList
# end tuples_from_FASTA_file

from re import sub

def spliced_DNA(seq, introns):
	"""Given a DNA sequence and a list of introns in the sequence, return the DNA sequence
	after excision of the introns."""
	pattern = "|".join([ "(" + intron + ")" for intron in introns ])
	return sub(pattern, "", seq)
# end spliced_DNA

def transcribe_DNA(seq):
	"""Given a DNA string t, return the transcribed RNA string of t."""
	return seq.replace("T", "U")
# end transcribe_DNA

def translate_mRNA_to_protein(seq):
	"""Given an RNA string s corresponding to a strand of mRNA, return the protein string encoded by s."""
	tDict = { "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V", "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A", "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", "UAG" : "stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "stop", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" }
	pos = 0
	protein = []
	while(pos < len(seq)):
		endOfSlice = pos + 3
		if(endOfSlice > len(seq)):
			print "Error translating mRNA: ran out of nucleotides, without a stop codon in sight!"
			return ""
		elif(not (seq[pos:endOfSlice] in tDict.keys())):
			print("Error translating mRNA: a bad codon was discovered somewhere in your mRNA sequence.")
			return ""
		elif(tDict[seq[pos:endOfSlice]] == "stop"):
			break
		protein.append(tDict[seq[pos:endOfSlice]])
		pos = pos + 3
	return "".join(protein)
# end translate_mRNA_to_protein

# main block
fTupleList = tuples_from_FASTA_file(raw_input("Path to Rosalind Input File (FASTA): ").strip())
print "Protein after excision of introns, transcription, and translation:"
print translate_mRNA_to_protein(transcribe_DNA(spliced_DNA(fTupleList[0][1], [seq for (seq_id, seq) in fTupleList[1:]])))

def dictionary_from_FASTA_file(filename):
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs. The file
	must end in a newline character; otherwise the last sequence will be missed!"""
	try:
		f = open(filename, "r")
	except IOError:
		print "A file does not exist at this location, or some other I/O error occurred."
		return ""
	fastaDict = { }
	sequence_id = 0
	naSequence = ""
	for line in f:
		if(line[0] == ">"):
			if(sequence_id != 0):
				fastaDict[sequence_id] = naSequence
			sequence_id = line[1:-1]
			naSequence = ""
		else:
			naSequence += line[:-1]
	fastaDict[sequence_id] = naSequence # last id:sequence pair, hanging around
	return fastaDict
# end dictionary_from_FASTA_file

def reverse_complement(seq):
	"""Given: a DNA string seq, return the reverse complement of seq."""
	rev = seq[::-1]
	complements = { "G":"C", "C":"G", "A":"T", "T":"A" }
	return "".join([complements[base] for base in rev])
# end reverse_complement

import re

def transcribe_DNA(seq):
	"""Given a DNA string t, return the transcribed RNA string of t."""
	return seq.replace("T", "U")
# end transcribe_DNA

def translate_mRNA_to_protein(seq):
	"""Given an RNA string seq corresponding to a strand of mRNA, return the protein string encoded by seq."""
	tDict = { "UUU":"F",
	"CUU":"L",
	"AUU":"I",
	"GUU":"V",
	"UUC":"F",
	"CUC":"L",
	"AUC":"I",
	"GUC":"V",
	"UUA":"L",
	"CUA":"L",
	"AUA":"I",
	"GUA":"V",
	"UUG":"L",
	"CUG":"L",
	"AUG":"M",
	"GUG":"V",
	"UCU":"S",
	"CCU":"P",
	"ACU":"T",
	"GCU":"A",
	"UCC":"S",
	"CCC":"P",
	"ACC":"T",
	"GCC":"A",
	"UCA":"S",
	"CCA":"P",
	"ACA":"T",
	"GCA":"A",
	"UCG":"S",
	"CCG":"P",
	"ACG":"T",
	"GCG":"A",
	"UAU":"Y",
	"CAU":"H",
	"AAU":"N",
	"GAU":"D",
	"UAC":"Y",
	"CAC":"H",
	"AAC":"N",
	"GAC":"D",
	"UAA":"stop",
	"CAA":"Q",
	"AAA":"K",
	"GAA":"E",
	"UAG":"stop",
	"CAG":"Q",
	"AAG":"K",
	"GAG":"E",
	"UGU":"C",
	"CGU":"R",
	"AGU":"S",
	"GGU":"G",
	"UGC":"C",
	"CGC":"R",
	"AGC":"S",
	"GGC":"G",
	"UGA":"stop",
	"CGA":"R",
	"AGA":"R",
	"GGA":"G",
	"UGG":"W",
	"CGG":"R",
	"AGG":"R",
	"GGG":"G"}
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

def open_reading_frames_dna(seq):
	"""Given a string representing a DNA sequence, return a list of all possible open reading frames associated with the sequence.
	This function returns open reading frames from the sequence itself and its reverse complement."""
	frames = []
	reReadingFrame = "(ATG(([AGCT]){3})*?(TAG|TGA|TAA))"
	frames.extend(re.findall("(?=%s)" % reReadingFrame, seq))
	frames.extend(re.findall("(?=%s)" % reReadingFrame, reverse_complement(seq)))
	return [frame for (frame, a, b, c) in frames]
# end open_reading_frames_dna

def proteins_from_dna_list_unique(sequences):
	"""Given a list of DNA sequences, return the unique proteins they encode directly as a list.
	Transcription and translation are both accomplished by this function."""
	proteins = [translate_mRNA_to_protein(transcribe_DNA(seq)) for seq in sequences]
	return list(set(proteins)) # return only unique proteins
# end proteins_from_dna_list_unique

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File (FASTA): ").strip())
for seq_id in fDict:
	print "Open reading frames in " + seq_id + ":"
	print "\n".join(proteins_from_dna_list_unique(open_reading_frames_dna(fDict[seq_id])))
	# print "\n".join(open_reading_frames_dna(fDict[seq_id]))
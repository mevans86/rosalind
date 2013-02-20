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

import re

def indices_of_noncontiguous_subsequence_dna(motif, seq):
	"""Given a motif, searches for non-contiguous subsequences corresponding to the
	motif in the given DNA string. Returns a list of tuples containing 1-indexed
	positions of nucleotides in each hit."""
	reMotif = "((" + ").*?(".join(list(motif)) + "))"
	hitList = []
	for match in re.finditer("(?=%s)" % reMotif, seq):
		hitList.append(tuple([match.start(i) + 1 for i in range(2, len(match.groups()) + 1)])) # why start at 2? Maybe 1-indexed?
	return hitList
# end indices_of_noncontiguous_subsequence_dna	

# main block
fTuples = tuples_from_FASTA_file(raw_input("Path to Rosalind Input File (FASTA): ").strip())
motif = fTuples[1][1]
seq = fTuples[0][1]
print "Non-contiguous locations of motif in sequence:"
print indices_of_noncontiguous_subsequence_dna(motif, seq)
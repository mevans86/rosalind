import itertools
import math
import re

def dictionary_from_FASTA_file(filename):
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs. The file
	must end in a newline character; otherwise the last sequence will not be read!"""
	try:
		f = open(filename, "r")
	except IOError:
		print "A file does not exist at this location, or some other I/O error occurred."
		return { }
	fastaDict = { }
	seq_id = 0
	seq = ""
	for line in f:
		if(line[0] == ">"):
			if(seq_id != 0):
				fastaDict[seq_id] = seq
			seq_id = line[1:-1]
			seq = ""
		else:
			seq += line[:-1]
	fastaDict[seq_id] = seq # last id:sequence pair, hanging around
	return fastaDict
# end dictionary_from_FASTA_file

def sorted_sequences(alphabet, length):
	"""Returns a list of tuples, each of which is a sequence of length length with letters
	contained in the given alphabet. Tuples are sorted alphabetically, based on the alphabet
	string provided."""
	return list(itertools.product(alphabet, repeat=length))
# end sorted_sequences

def count_matches(pattern, naStr):
	"""Returns the number of times pattern is found in naStr, including overlapping hits."""
	count = 0
	for hit in re.finditer("(?=%s)" % pattern, naStr):
		count = count + 1
	return count
# end count_matches

# main block
filename = raw_input("Path to Rosalind Input File: ").strip()
fDict = dictionary_from_FASTA_file(filename)
naStr = fDict[fDict.keys()[0]]

print "4-mer composition of the given sequence:"
print " ".join([str(count_matches("".join(seq), naStr)) for seq in sorted_sequences("ACGT", 4)])
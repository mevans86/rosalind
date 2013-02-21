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

def reverse_complement(seq):
	"""Given: a DNA string seq, return the reverse complement of seq."""
	rev = seq[::-1]
	complements = { "G":"C", "C":"G", "A":"T", "T":"A" }
	return "".join([complements[base] for base in rev])
# end reverse_complement

def restriction_sites(seq, minLength, maxLength):
	"""Given a DNA string seq, return a list of tuples containing the location and identity
	(respectively) of restriction sites in the sequence between minLength and maxLength."""
	sites = []
	for i in range(len(seq)):
		for l in range(minLength, maxLength + 1):
			if(i+l <= len(seq)):
				subseq = seq[i:i+l]
				if(subseq == reverse_complement(subseq)):
					if(len(subseq) >= minLength and len(subseq) <= maxLength):
						sites.append((i+1, subseq))
	return sites
# end restriction_sites

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File (FASTA): ").strip())
print "Restriction sites in the provided sequence:"
print "\n".join(["%d %s" % (l, len(seq)) for (l, seq) in restriction_sites(fDict[fDict.keys()[0]], 4, 12)])

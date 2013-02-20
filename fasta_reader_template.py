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

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File (FASTA): ").strip())

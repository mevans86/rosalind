def dictionary_from_FASTA_file(filename):
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs."""
	try:
		f = open(filename, "r")
	except IOError:
		print "A file does not exist at this location, or some other I/O error occurred."
		return { }
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

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File: ").strip())

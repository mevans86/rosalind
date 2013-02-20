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
def dictionary_from_FASTA_file(filename):
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs. The file
	must end in a newline character; otherwise the last sequence will be missed!"""
	try:
		f = open(filename, "r")
	except IOError:
		print "A file does not exist at this location, or some other I/O error occurred."
		return ""
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

def transition_transversion_ratio(seqA, seqB):
	"""Given two DNA strings, return the ratio of transitions (purine-purine or pyrimidine-pyrimidine)
	to transversions (purine-pyrimidine) between the two strings. Strings must match in length."""
	purines = ["A", "G"]
	pyrimidines = ["C", "T"]
	transitions = 0
	transversions = 0
	if(len(seqA) != len(seqB)):
		print "Error while calculating transition-transversion ratio: sequences must have identical length."
		return -1
	for i in range(len(seqA)):
		if(seqA[i] in purines):
			if(seqB[i] in purines and seqA[i] != seqB[i]):
				transitions += 1
			elif(seqB[i] in pyrimidines):
				transversions += 1
		if(seqA[i] in pyrimidines):
			if(seqB[i] in pyrimidines and seqA[i] != seqB[i]):
				transitions += 1
			elif(seqB[i] in purines):
				transversions += 1
	return float(transitions) / transversions
# end transition_transversion_ratio

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File (FASTA): ").strip())
if(len(fDict.keys()) != 2):
	print "Error while calculating transition-transversion ratio: exactly two sequences must be provided in FASTA format."
	sys.exit()
print "Transition-transversion ratio:"
print transition_transversion_ratio(fDict[fDict.keys()[0]], fDict[fDict.keys()[1]])
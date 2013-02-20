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

def overlap_graph(sequenceDictionary, overlapLength):
	"""Given a dictionary of id:sequences, return an n x 2 matrix of adjacencies representing an
	overlap graph (for overlaps of length overlapLength) for the given sequences."""
	if(sequenceDictionary.keys() == []):
		return "Error when determining overlap graph: provided dictionary is empty."
		return []

	adjacencies = []
	for id1 in sequenceDictionary.keys():
		if(overlapLength > len(sequenceDictionary[id1])):
			print "Error when determining overlap graph: overlapLength must be less than all sequence lengths."
			return []
		for id2 in sequenceDictionary.keys():
			if(not id1 == id2):
				if(sequenceDictionary[id1][-overlapLength:] == sequenceDictionary[id2][:overlapLength]):
					adjacencies.append((id1, id2))
	return adjacencies
# end overlap_graph

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File (FASTA): ").strip())
print "Adjacencies of overlap graph for length = 3:"
for edge in overlap_graph(fDict, 3):
	print edge[0] + " " + edge[1]

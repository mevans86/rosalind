def dictionary_from_FASTA_file(filename):
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs. The file
	must end with a new line character; otherwise, the last sequence will be missed!"""
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

def longest_common_substr(listOfStrings):
	"""Given a list of strings, return the longest substring common to all of them."""
	substr = ""
	if len(listOfStrings) > 1 and len(listOfStrings[0]) > 0:
		for i in range(len(listOfStrings[0])):
			for j in range(len(listOfStrings[0])-i+1):
				if j > len(substr) and all(listOfStrings[0][i : i + j] in x for x in listOfStrings):
					substr = listOfStrings[0][i : i + j]
	return substr
# end longest_common_substr

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File: ").strip())
print "Longest motif common to all sequences:"
print longest_common_substr(fDict.values())
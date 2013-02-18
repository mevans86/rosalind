def dictionaryFromFASTAFile(filename):
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs."""
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
# end dictionaryFromFASTAFile

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
fDict = dictionaryFromFASTAFile(raw_input("Path to Rosalind Input File: ").strip())
print "Longest motif common to all sequences: " + longest_common_substr(fDict.values())
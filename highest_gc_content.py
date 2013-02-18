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

def percentGC(dnaString):
	"""Given a continuous DNA sequence, returns the percentage of G and C nucleotides."""
	return (dnaString.count("G") + dnaString.count("C")) / float(len(dnaString)) * 100
# end percentGC

# main block
fDict = dictionaryFromFASTAFile(raw_input("Path to Rosalind Input File: ").strip())
maxGC = 0
idOfmaxGC = ""
for seq_id in fDict.keys():
	currentGC = percentGC(fDict[seq_id])
	if(currentGC > maxGC):
		maxGC = currentGC
		idOfmaxGC = seq_id
print "NA sequence with maximum GC content:"
print str(idOfmaxGC) + "\n" + str(maxGC)
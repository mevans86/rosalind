def dictionary_from_FASTA_file(filename):
<<<<<<< HEAD
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs. The file
	must end with a new line character; otherwise, the last sequence will be missed!"""
=======
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs."""
>>>>>>> Consensus & profile; FASTA reader template
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

<<<<<<< HEAD
def percent_GC(seq):
	"""Given a continuous DNA sequence, returns the percentage of G and C nucleotides."""
	return (seq.count("G") + seq.count("C")) / float(len(seq)) * 100
=======
def percent_GC(dnaString):
	"""Given a continuous DNA sequence, returns the percentage of G and C nucleotides."""
	return (dnaString.count("G") + dnaString.count("C")) / float(len(dnaString)) * 100
>>>>>>> Consensus & profile; FASTA reader template
# end percent_GC

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File: ").strip())
maxGC = 0
idOfmaxGC = ""
for seq_id in fDict.keys():
	currentGC = percent_GC(fDict[seq_id])
	if(currentGC > maxGC):
		maxGC = currentGC
		idOfmaxGC = seq_id
print "Sequence with greatest GC content:"
print idOfmaxGC
print maxGC

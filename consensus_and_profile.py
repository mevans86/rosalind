def dictionary_from_FASTA_file(filename):
	"""Given a path to a FASTA file, returns a dictionary of id:sequence key-value pairs. The FASTA file
	must end in a newline character!"""
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

def profile_matrix_DNA(dna_strings_list):
	"""Given a list of DNA sequences, return the profile matrix for the list."""
	pMatrix = { }
	if(not len(dna_strings_list) > 0):
		print "Error generating profile matrix: array of DNA sequences is empty."
		return pMatrix
	for sequence in dna_strings_list:
		for i in range(len(sequence)):
			if(sequence[i] == "A"):
				if(not 0 in pMatrix.keys()):
					pMatrix[0] = [ 0 ] * len(sequence)
				pMatrix[0][i] += 1
			elif(sequence[i] == "C"):
				if(not 1 in pMatrix.keys()):
					pMatrix[1] = [ 0 ] * len(sequence)
				pMatrix[1][i] += 1
			elif(sequence[i] == "G"):
				if(not 2 in pMatrix.keys()):
					pMatrix[2] = [ 0 ] * len(sequence)
				pMatrix[2][i] += 1
			elif(sequence[i] == "T"):
				if(not 3 in pMatrix.keys()):
					pMatrix[3] = [ 0 ] * len(sequence)
				pMatrix[3][i] += 1
	return pMatrix
# end profile_matrix_DNA

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File: ").strip())
seqList = fDict.values()
print "Profile matrix for input:"
print "A: " + str(profile_matrix_DNA(seqList)[0])
print "C: " + str(profile_matrix_DNA(seqList)[1])
print "G: " + str(profile_matrix_DNA(seqList)[2])
print "T: " + str(profile_matrix_DNA(seqList)[3])
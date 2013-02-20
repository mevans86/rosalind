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

def profile_matrix_dna(dnaStrings):
	"""Given a list of DNA sequences, return the profile matrix for the list."""
	pMatrix = { }
	if(not len(dnaStrings) > 0):
		print "Error generating profile matrix: array of DNA sequences is empty."
		return pMatrix
	for sequence in dnaStrings:
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
# end profile_matrix_dna

def consensus_string_dna(profileMatrix):
	"""Given a profile matrix for a set of DNA strings, return a consensus
	string for the collection. Not ideal at this point."""
	maxBaseIndices = [None]*len(profileMatrix[0])
	for i in range(len(profileMatrix[0])):
		currMax = 0
		for j in range(4):
			if(max(currMax, profileMatrix[j][i]) > currMax):
				currMax = max(currMax, profileMatrix[j][i])
				maxBaseIndices[i] = str(j)
	return "".join(maxBaseIndices).replace("0", "A").replace("1", "C").replace("2", "G").replace("3", "T")
# end consensus_string_dna

# main block
fDict = dictionary_from_FASTA_file(raw_input("Path to Rosalind Input File: ").strip())
seqList = fDict.values()
print "Profile matrix for input:"
print "A: " + str(profile_matrix_dna(seqList)[0])
print "C: " + str(profile_matrix_dna(seqList)[1])
print "G: " + str(profile_matrix_dna(seqList)[2])
print "T: " + str(profile_matrix_dna(seqList)[3])
print "Consensus string:"
print consensus_string_dna(profile_matrix_dna(seqList))
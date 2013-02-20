<<<<<<< HEAD
def hamming_distance(seqA, seqB):
=======
def hamming_distance(sequenceA, sequenceB):
>>>>>>> Consensus & profile; FASTA reader template
	"""Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
	
	Returns: The Hamming distance dH(s,t). Given two strings s and t of equal length, the
	Hamming distance between s and t is the number of corresponding symbols that differ
	in s and t."""

	if(len(seqA) != len(seqB)):
		print "Error calculating Hamming distance: provided DNA sequences are not equal in length!"
		return -1

	counter = 0
	distance = 0
	for nucleotide in seqA:
		if(nucleotide != "A" and nucleotide != "T" and nucleotide != "G" and nucleotide != "C"):
			print "Error calculating Hamming distance: malformed DNA sequence."
			return -1
		if(nucleotide != seqB[counter]):
			distance += 1
		counter += 1
	return distance
# end hamming_distance

# main block
try:
	f = open(raw_input("Path to Rosalind Input File: ").strip(), "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
<<<<<<< HEAD
print "Hamming distance:"
print hamming_distance(f.readline()[:-1], f.readline()[:-1])
=======

dist = hamming_distance(f.readline()[:-1], f.readline()[:-1])
print "\nHamming distance: " + str(dist) + "\n"
>>>>>>> Consensus & profile; FASTA reader template

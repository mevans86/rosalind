def hammingDistance(sequenceA, sequenceB):
	"""Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
	
	Returns: The Hamming distance dH(s,t). Given two strings s and t of equal length, the
	Hamming distance between s and t is the number of corresponding symbols that differ
	in s and t."""

	if(len(sequenceA) != len(sequenceB)):
		print "Error calculating Hamming distance: provided DNA sequences are not equal in length!"
		return -1

	counter = 0
	distance = 0
	for nucleotide in sequenceA:
		if(nucleotide != "A" and nucleotide != "T" and nucleotide != "G" and nucleotide != "C"):
			print "Error calculating Hamming distance: malformed DNA sequence."
			return -1
		if(nucleotide != sequenceB[counter]):
			distance += 1
		counter += 1
	return distance
# end hammingDistance

# main block
filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()

dist = hammingDistance(f.readline()[:-1], f.readline()[:-1])
print "\nHamming distance: " + str(dist) + "\n"
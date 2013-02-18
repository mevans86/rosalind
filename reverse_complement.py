def reverseComplement(DNAstring):
	"""Given: A DNA string s of length at most 1000 bp.
			
	Return: The reverse complement sc of s."""

	reversedSequence = DNAstring[::-1]
	complement = { "G" : "C", "C" : "G", "A": "T", "T": "A" }
	reversedSequenceList = []
	for base in reversedSequence[:]:
		reversedSequenceList.extend(base)
	return "".join([complement[base] for base in reversedSequenceList])

filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()

rcSeq = reverseComplement(f.readline()[:-1])
print "\nReverse complement of the sequence provided: " + str(rcSeq) + "\n"
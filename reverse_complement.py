<<<<<<< HEAD
def reverse_complement(seq):
	"""Given: a DNA string seq, return the reverse complement of seq."""
	rev = seq[::-1]
	complements = { "G":"C", "C":"G", "A":"T", "T":"A" }
	return "".join([complements[base] for base in rev])
# end reverse_complement
=======
def reverse_complement_DNA(DNAstring):
	"""Given: A DNA string s of length at most 1000 bp.
			
	Return: The reverse complement sc of s."""
>>>>>>> Consensus & profile; FASTA reader template

# main block
try:
	f = open(raw_input("Path to Rosalind Input File: ").strip(), "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
<<<<<<< HEAD
print "Reverse complement of the sequence provided:"
print reverse_complement(f.readline()[:-1])
=======

rcSeq = reverse_complement_DNA(f.readline()[:-1])
print "\nReverse complement of the sequence provided: " + str(rcSeq) + "\n"
>>>>>>> Consensus & profile; FASTA reader template

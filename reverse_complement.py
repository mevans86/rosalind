def reverse_complement(seq):
	"""Given: a DNA string seq, return the reverse complement of seq."""
	rev = seq[::-1]
	complements = { "G":"C", "C":"G", "A":"T", "T":"A" }
	return "".join([complements[base] for base in rev])
# end reverse_complement

# main block
try:
	f = open(raw_input("Path to Rosalind Input File: ").strip(), "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
print "Reverse complement of the sequence provided:"
print reverse_complement(f.readline()[:-1])
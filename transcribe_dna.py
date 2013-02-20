def transcribe_DNA(seq):
	"""Given a DNA string t, return the transcribed RNA string of t."""
	return seq.replace("T", "U")
# end transcribe_DNA

filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
print "mRNA derived from provided DNA:"
print transcribe_DNA(f.readline()[:-1])
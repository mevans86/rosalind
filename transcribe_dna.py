def transcribeDNA(dnaSequence):
	"""Given: A DNA string t having length at most 1000 nt.
			
	Return: The transcribed RNA string of t."""
	
	return dnaSequence.replace("T", "U")
# end transcribeDNA

filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()

mrnaSeq = transcribeDNA(f.readline())
print "\nmRNA derived from provided DNA: " + str(mrnaSeq) + "\n"
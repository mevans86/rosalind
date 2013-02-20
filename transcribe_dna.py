<<<<<<< HEAD
def transcribe_DNA(seq):
	"""Given a DNA string t, return the transcribed RNA string of t."""
	return seq.replace("T", "U")
=======
def transcribe_DNA(dnaSequence):
	"""Given: A DNA string t having length at most 1000 nt.
			
	Return: The transcribed RNA string of t."""
	
	return dnaSequence.replace("T", "U")
>>>>>>> Consensus & profile; FASTA reader template
# end transcribe_DNA

filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
<<<<<<< HEAD
print "mRNA derived from provided DNA:"
print transcribe_DNA(f.readline()[:-1])
=======

mrnaSeq = transcribe_DNA(f.readline())
print "\nmRNA derived from provided DNA: " + str(mrnaSeq) + "\n"
>>>>>>> Consensus & profile; FASTA reader template

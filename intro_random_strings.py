import math

def probability_of_random_match_gc(motif, gcContent):
	"""Given a DNA sequence motif and a target GC content, return the probability
	that a random string with the given GC content matches the motif exactly."""
	probability = 1.0
	for base in motif:
		if(base == "G" or base == "C"):
			probability *= gcContent / 2.0
		elif(base == "A" or base == "T"):
			probability *= (1.0 - gcContent) / 2.0
	return probability
# end probability_of_random_match_gc

# main block
try:
	f = open(raw_input("Path to Rosalind Input File: ").strip(), "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred."
	sys.exit()
seq = f.readline()[:-1]
gcFreqs = [float(freq) for freq in f.readline()[:-1].split(" ")]
print "Log10 likelihoods of exact match between motif %s and random strings with given GC contents:" % seq
print " ".join([str(math.log10(probability_of_random_match_gc(seq, freq))) for freq in gcFreqs])
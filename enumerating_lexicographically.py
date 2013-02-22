import itertools
import math

def sorted_sequences(alphabet, length):
	return list(itertools.product(alphabet, repeat=length))
# end sorted_sequences

# main block
filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
alphabet = "".join(f.readline().split(" "))[:-1]
length = int(f.readline())
print "Possible sequences of length %d from alphabet %s:" % (length, alphabet)
print "\n".join(["".join(seq) for seq in sorted_sequences(alphabet, length)])
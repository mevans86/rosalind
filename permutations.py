import itertools
import math

def list_of_permutations(n):
	"""Lists all possible permutations of 1, 2, 3, ..., n."""
	return list(itertools.permutations([k for k in range(1, n+1)]))
# end list_of_permutations

def number_of_permutations(n):
	"""Returns the number of permutations of n items."""
	return math.factorial(n)
# end number_of_permutations

# main block
filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
n = int(f.readline())
print "Possible permutations of %d objects:" % n
print number_of_permutations(n)
print "\n".join([" ".join([str(item) for item in perm]) for perm in list_of_permutations(n)])
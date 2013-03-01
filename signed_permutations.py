import itertools
import math

def list_of_signed_permutations(n):
	"""Lists all possible signed permutations of +-1, 2, 3, ..., n."""
	ret = [ ]
	for mult in list(itertools.product([-1, 1], repeat=n)):
		for perm in list(itertools.permutations(range(1, n+1))):
			ret.append(tuple([x * y for x, y in zip(list(mult), perm)]))
	return ret
# end list_of_permutations

def number_of_signed_permutations(n):
	"""Returns the number of signed permutations of n items."""
	return math.factorial(n) * 2**n
# end number_of_signed_permutations

# main block
filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
n = int(f.readline())
print "Possible signed permutations of %d objects:" % n
print number_of_signed_permutations(n)
print "\n".join([" ".join([str(item) for item in perm]) for perm in list_of_signed_permutations(n)])
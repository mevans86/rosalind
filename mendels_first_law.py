import sys

def probabilityOfDominantPhenotype(KMNstring):	
	"""Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
	k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
	
	Returns: The probability that two randomly selected mating organisms will produce an individual possessing
	a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate."""

	homozygousDominantCount = int(KMNstring.split(" ")[0])
	heterozygousCount = int(KMNstring.split(" ")[1])
	homozygousRecessiveCount = int(KMNstring.split(" ")[2])
	total = homozygousDominantCount + heterozygousCount + homozygousRecessiveCount
	if(total < 2):
		return 0
	
	DomDomProbability = homozygousDominantCount / float(total)
	HetProbability = heterozygousCount / float(total)
	RecRecProbability = homozygousRecessiveCount / float(total)

	finalProbability = DomDomProbability
	finalProbability += (HetProbability * homozygousDominantCount / (total - 1.0))
	finalProbability += (HetProbability * (heterozygousCount - 1.0) / (total - 1.0) * 0.75)
	finalProbability += (HetProbability * homozygousRecessiveCount / (total - 1.0) * 0.5)
	finalProbability += (RecRecProbability * homozygousDominantCount / (total - 1.0))
	finalProbability += (RecRecProbability * heterozygousCount / (total - 1.0) * 0.5)
	
	return finalProbability
# end probabilityOfDominantPhenotype

filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()

prob = probabilityOfDominantPhenotype(f.readline())
print "\nProbability of the dominant phenotype: " + str(prob) + "\n"
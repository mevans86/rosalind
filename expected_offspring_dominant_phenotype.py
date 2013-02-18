def expectedOffspringWithDominantPhenotype(arrayOfGenotypeCounts):
	"""Given: Six positive integers, each of which does not exceed 20,000. The integers correspond
	to the number of couples in a population possessing each genotype pairing for a given factor.
	In order, the six given integers represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

	Return: The expected number of offspring displaying the dominant phenotype in the next generation,
	under the assumption that every couple has exactly two offspring."""

	expectedDominantPhenotypes = int(arrayOfGenotypeCounts[0])
	expectedDominantPhenotypes += int(arrayOfGenotypeCounts[1])
	expectedDominantPhenotypes += int(arrayOfGenotypeCounts[2])
	expectedDominantPhenotypes += int(arrayOfGenotypeCounts[3]) * 0.75
	expectedDominantPhenotypes += int(arrayOfGenotypeCounts[4]) * 0.5
	expectedDominantPhenotypes += int(arrayOfGenotypeCounts[5]) * 0

	return expectedDominantPhenotypes * 2
# end expectedOffspring

filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()

couplesGenotypesArray = f.readline().split(" ")
exp = expectedOffspringWithDominantPhenotype(couplesGenotypesArray)
print "Expected number of offspring displaying the dominant phenotype (assuming two offspring per couple): " + str(exp)
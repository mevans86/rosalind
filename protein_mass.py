def mass_protein(proteinString):
	"""Given: A protein string P of length at most 1000 aa.
			
	Return: The weight of P. Consult the monoisotopic mass table."""

	proteinMasses = {"A": 71.03711,
	"C": 103.00919,
	"D": 115.02694,
	"E": 129.04259,
	"F": 147.06841,
	"G": 57.02146,
	"H": 137.05891,
	"I": 113.08406,
	"K": 128.09496,
	"L": 113.08406,
	"M": 131.04049,
	"N": 114.04293,
	"P": 97.05276,
	"Q": 128.05858,
	"R": 156.10111,
	"S": 87.03203,
	"T": 101.04768,
	"V": 99.06841,
	"W": 186.07931,
	"Y": 163.06333}

	ret = 0.0
	for residue in proteinString:
		if(residue in proteinMasses.keys()):
			ret += proteinMasses[residue]
		else:
			print "Error calculating protein mass: unknown amino acid abbreviation. Stick to the twenty natural amino acids."
			return -1;
	return ret
# end mass_protein

# main block
filename = raw_input("Path to Rosalind Input File: ").strip()
try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()

m = mass_protein(f.readline()[:-1])
print "\nMass of protein: " + str(m) + "\n"
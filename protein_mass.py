def mass_protein(protein):
	"""Given a protein string, return the average mass of the protein."""
	aminoAcidMasses = {"A":71.03711,
	"C":103.00919,
	"D":115.02694,
	"E":129.04259,
	"F":147.06841,
	"G":57.02146,
	"H":137.05891,
	"I":113.08406,
	"K":128.09496,
	"L":113.08406,
	"M":131.04049,
	"N":114.04293,
	"P":97.05276,
	"Q":128.05858,
	"R":156.10111,
	"S":87.03203,
	"T":101.04768,
	"V":99.06841,
	"W":186.07931,
	"Y":163.06333}
	ret = 0.0
	for residue in protein:
		if(residue in aminoAcidMasses.keys()):
			ret += aminoAcidMasses[residue]
		else:
			print "Error calculating protein mass: unknown amino acid abbreviation. Stick to the twenty natural amino acids."
			return -1;
	return ret
# end mass_protein

# main block
try:
	f = open(raw_input("Path to Rosalind Input File: ").strip(), "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
print "Mass of protein:"
print mass_protein(f.readline()[:-1])
<<<<<<< HEAD
def translate_mRNA_to_protein(seq):
	"""Given an RNA string seq corresponding to a strand of mRNA, return the protein string encoded by seq."""
	tDict = { "UUU":"F",
	"CUU":"L",
	"AUU":"I",
	"GUU":"V",
	"UUC":"F",
	"CUC":"L",
	"AUC":"I",
	"GUC":"V",
	"UUA":"L",
	"CUA":"L",
	"AUA":"I",
	"GUA":"V",
	"UUG":"L",
	"CUG":"L",
	"AUG":"M",
	"GUG":"V",
	"UCU":"S",
	"CCU":"P",
	"ACU":"T",
	"GCU":"A",
	"UCC":"S",
	"CCC":"P",
	"ACC":"T",
	"GCC":"A",
	"UCA":"S",
	"CCA":"P",
	"ACA":"T",
	"GCA":"A",
	"UCG":"S",
	"CCG":"P",
	"ACG":"T",
	"GCG":"A",
	"UAU":"Y",
	"CAU":"H",
	"AAU":"N",
	"GAU":"D",
	"UAC":"Y",
	"CAC":"H",
	"AAC":"N",
	"GAC":"D",
	"UAA":"stop",
	"CAA":"Q",
	"AAA":"K",
	"GAA":"E",
	"UAG":"stop",
	"CAG":"Q",
	"AAG":"K",
	"GAG":"E",
	"UGU":"C",
	"CGU":"R",
	"AGU":"S",
	"GGU":"G",
	"UGC":"C",
	"CGC":"R",
	"AGC":"S",
	"GGC":"G",
	"UGA":"stop",
	"CGA":"R",
	"AGA":"R",
	"GGA":"G",
	"UGG":"W",
	"CGG":"R",
	"AGG":"R",
	"GGG":"G"}
	pos = 0
	protein = []
	while(pos < len(seq)):
		endOfSlice = pos + 3
		if(endOfSlice > len(seq)):
			print "Error translating mRNA: ran out of nucleotides, without a stop codon in sight!"
			return ""
		elif(not (seq[pos:endOfSlice] in tDict.keys())):
			print("Error translating mRNA: a bad codon was discovered somewhere in your mRNA sequence.")
			return ""
		elif(tDict[seq[pos:endOfSlice]] == "stop"):
			break
		protein.append(tDict[seq[pos:endOfSlice]])
		pos = pos + 3
	return "".join(protein)
=======
def translate_mRNA_to_protein(mRNAstring):
	"""Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

	Return: The protein string encoded by s."""
	
	translationDictionary = { "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V", "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A", "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" }
	loopPosition = 0
	aminoAcidList = []
	error = 0
	while(loopPosition < len(mRNAstring)):
		endOfSlice = loopPosition + 3
		if(not (mRNAstring[loopPosition:endOfSlice] in translationDictionary.keys())):
			print("Error translating mRNA: a bad codon was discovered somewhere in your mRNA sequence!")
			error = 1
			break
		if(translationDictionary[mRNAstring[loopPosition:endOfSlice]] == "Stop"):
			break
		aminoAcidList.append(translationDictionary[mRNAstring[loopPosition:endOfSlice]])
		loopPosition = loopPosition + 3
	if(error == 0):	
		return "".join(aminoAcidList)
	else:
		return "Error"
>>>>>>> Consensus & profile; FASTA reader template
# end translate_mRNA_to_protein

# main block
try:
	f = open(raw_input("Path to Rosalind Input File: ").strip(), "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
<<<<<<< HEAD
print "Translated protein:"
print translate_mRNA_to_protein(f.readline()[:-1])
=======

proteinSeq = translate_mRNA_to_protein(f.readline())
print "\nTranslated protein: " + str(proteinSeq) + "\n"
>>>>>>> Consensus & profile; FASTA reader template

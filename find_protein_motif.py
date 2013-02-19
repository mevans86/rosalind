import sys
import re
import urllib2

def parseFASTAString(fastaString):
	"""Given a string in FASTA format, return a dictionary of id:sequence key-value pairs."""
	fastaDict = { }
	sequence_id = 0
	seq = ""
	for line in fastaString.split("\n"):
		if(len(line) > 0 and str(line)[0] == ">"):
			if(sequence_id != 0):
				fastaDict[sequence_id] = seq
			sequence_id = line[1:]
			seq = ""
		else:
			seq += line
	fastaDict[sequence_id] = seq # last id:sequence pair, hanging around
	return fastaDict
# end parseFASTAString

def dictionaryFromFASTAURL(fastaURL):
	"""Given a URL to a FASTA file, returns a dictionary of id:sequence key-value pairs."""
	try:
		response = urllib2.urlopen(fastaURL)
	except:
		print "Error accessing Uniprot: bad ID provided."
		sys.exit()
	fastaString = response.read()

	return parseFASTAString(fastaString)
# end dictionaryFromFASTAURL

def find_protein_motif(motifString, proteinSequence):
	"""Given a string representing a protein motif and a full sequence of amino acid residues, return
	positions (1-indexed!) where the motif is found in the sequence as a space-separated list."""

	regExpMotif = re.sub(r"\{(.)\}", r"[^\1]", motifString)
	output = ""
	for hit in re.finditer('(?=%s)' % regExpMotif, proteinSequence):
		output += (str(hit.start() + 1) + " ")
	return output.strip()
# end find_protein_motif

# main block
filename = raw_input("Path to Rosalind Input File: ").strip()

try:
	f = open(filename, "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()

for line in f:
	fDict = dictionaryFromFASTAURL("http://www.uniprot.org/uniprot/%s.fasta" % line[:-1])
	protSeq = fDict[fDict.keys()[0]] # get the first protein sequence listed at the URL
	if(find_protein_motif("N{P}[ST]{P}", protSeq) != ""):
		print line[:-1]
		print find_protein_motif("N{P}[ST]{P}", protSeq)
	
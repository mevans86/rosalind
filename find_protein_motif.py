import re
import urllib2

<<<<<<< HEAD
def parse_FASTA_string(fasta):
=======
def dictionaryFromFASTAString(fastaString):
>>>>>>> Consensus & profile; FASTA reader template
	"""Given a string in FASTA format, return a dictionary of id:sequence key-value pairs."""
	fastaDict = { }
	seq_id = 0
	seq = ""
	for line in fasta.split("\n"):
		if(len(line) > 0 and str(line)[0] == ">"):
			if(seq_id != 0):
				fastaDict[seq_id] = seq
			seq_id = line[1:]
			seq = ""
		else:
			seq += line
	fastaDict[seq_id] = seq # last id:sequence pair, hanging around
	return fastaDict
<<<<<<< HEAD
# end parse_FASTA_string
=======
# end dictionaryFromFASTAString
>>>>>>> Consensus & profile; FASTA reader template

def dictionary_from_FASTA_URL(fastaURL):
	"""Given a URL to a FASTA file, returns a dictionary of id:sequence key-value pairs."""
	try:
		response = urllib2.urlopen(fastaURL)
	except:
		print "Error accessing Uniprot: bad ID provided."
		sys.exit()
	fasta = response.read()

<<<<<<< HEAD
	return parse_FASTA_string(fasta)
=======
	return dictionaryFromFASTAString(fastaString)
>>>>>>> Consensus & profile; FASTA reader template
# end dictionary_from_FASTA_URL

def find_protein_motif(motifString, protein):
	"""Given a string representing a protein motif and a full sequence of amino acid residues, return
	positions (1-indexed!) where the motif is found in the sequence as a space-separated list."""

	reMotif = re.sub(r"\{(.)\}", r"[^\1]", motifString)
	output = ""
	for hit in re.finditer("(?=%s)" % reMotif, protein):
		output += (str(hit.start() + 1) + " ")
	return output.strip()
# end find_protein_motif

# main block
try:
	f = open(raw_input("Path to Rosalind Input File: ").strip(), "r")
except IOError:
	print "A file does not exist at this location, or some other I/O error occurred. Peace out!"
	sys.exit()
for line in f:
	fDict = dictionary_from_FASTA_URL("http://www.uniprot.org/uniprot/%s.fasta" % line[:-1])
	protSeq = fDict[fDict.keys()[0]] # get the first protein sequence listed at the URL
	if(find_protein_motif("N{P}[ST]{P}", protSeq) != ""):
		print line[:-1]
		print find_protein_motif("N{P}[ST]{P}", protSeq)
	
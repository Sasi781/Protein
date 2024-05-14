import urllib
uniprot_url = "https://www.uniprot.org/uniprot/{0}.fasta"
from Bio import Entrez

def get_smiles_from_cid(cid):
    return urllib.request.urlopen("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/%d/property/CanonicalSMILES/txt"%cid).read().decode("utf-8").strip()
 
def get_seq_from_uniprot_acc(uniprot_acc):
    opened = urllib.request.urlopen(uniprot_url.format(uniprot_acc))
    lines = opened.readlines()
    return "".join([line.decode("utf-8").rstrip() for line in lines[1:]])

def get_synonyms(cid):
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{}/synonyms/TXT".format(cid)
    response = urllib.request.urlopen(url)
    synonyms = response.read().decode("utf-8").strip().split("\n")
    return synonyms[:3]
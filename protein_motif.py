import requests as r
from Bio import SeqIO
from io import StringIO
import re

filename = "rosalind_mprt.txt"
proteins = []

def openFile(filename):
    '''Open a file'''
    f =open(filename)
    return f.readlines()


def getProteinSequence(cID,complete_entry):
    '''Acquire protein sequence from UniProt database. 

        If complete_entry is TRUE, then the complete record will be returned.\n
        If complete_entry is FALSE, then ONLY the PROTEIN SEQUENCE will be returned.
    '''
    baseUrl="http://www.uniprot.org/uniprot/"
    currentUrl=baseUrl+cID+".fasta"
    response = r.post(currentUrl)
    cData=''.join(response.text)

    Seq=StringIO(cData)
    pSeq=list(SeqIO.parse(Seq,'fasta'))

    if complete_entry==True:
        return pSeq
    elif pSeq!=[]:
        return pSeq[0].seq



def findGlycosylationMotif(sequence):
    pattern = re.compile('N[^P](?:S|T)[^P]')
    positions = []
    for y in pattern.finditer(sequence):
        positions.append(y.start()+1)
    
    return positions


def start(name):
    file_opened = openFile(name)

    for x in file_opened:
        proteins.append(x.strip('\n'))

    for y in proteins:
        protein = str(getProteinSequence(y,False))
        glyc = findGlycosylationMotif(protein)
        print(y)
        print(glyc)

test = getProteinSequence("P20840_SAG1_YEAST",True)
#print(test)

start(filename)
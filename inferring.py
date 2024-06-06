def fileProcessing(filename):
    f = open(filename)
    x = f.readline()
    x = x.strip()
    return x

def infer(filename):
    sequence = fileProcessing(filename)
    num = 0
    codons = {
    'A': ['GCA', 'GCC', 'GCG', 'GCT'],
    'C': ['TGC', 'TGT'],
    'D': ['GAC', 'GAT'],
    'E': ['GAA', 'GAG'],
    'F': ['TTC', 'TTT'],
    'G': ['GGA', 'GGC', 'GGG', 'GGT'],
    'H': ['CAC', 'CAT'],
    'I': ['ATA', 'ATC', 'ATT'],
    'K': ['AAA', 'AAG'],
    'L': ['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'],
    'M': ['ATG'],
    'N': ['AAC', 'AAT'],
    'P': ['CCA', 'CCC', 'CCG', 'CCT'],
    'Q': ['CAA', 'CAG'],
    'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'],
    'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'],
    'T': ['ACA', 'ACC', 'ACG', 'ACT'],
    'V': ['GTA', 'GTC', 'GTG', 'GTT'],
    'W': ['TGG'],
    'Y': ['TAC', 'TAT'],
    '_': ['TAA', 'TAG', 'TGA'],
    }

    chance = 1
    for amino in sequence:
        chance *= (len(codons[amino]))
        chance %= 1E6
        
    return chance*3 # multiplying by three accounts for potential variance in stop codons

probability = infer("rosalind_mrna.txt")
print(probability)
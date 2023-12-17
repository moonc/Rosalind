def openFile(filename):
    '''Open a file'''
    f =open(filename)
    return f.read()
    
nucleotides = openFile('rosalind_revc.txt')

sequence =""
rev_complement = ""

for c in reversed(nucleotides):
    sequence = sequence+c

for x in sequence:
    if x =='A':
        rev_complement = rev_complement + 'T'
    elif x =='T':
        rev_complement = rev_complement + 'A'
    elif x =='C':
        rev_complement = rev_complement + 'G'
    elif x =='G':
        rev_complement = rev_complement + 'C'

print(rev_complement)
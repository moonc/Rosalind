def openFile(filename):
    '''Open a file'''
    f =open(filename)
    return f.read()
    
nucleotides = openFile('rosalind_rna.txt')

sequence =""
for x in nucleotides:
    if x =='T':
        sequence = sequence+'U'
    else:
        sequence = sequence+x


print(nucleotides+'\n')
print(sequence)
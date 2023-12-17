a_count = 0
t_count = 0
c_count = 0
g_count = 0
def openFile(filename):
    '''Open a file'''
    f =open(filename)
    return f.read()
    
nucleotides = openFile('rosalind_dna.txt')
#print(nucleotides)


for x in nucleotides:
    if x =='A':
        a_count += 1
    elif x =='T':
        t_count += 1
    elif x =='C':
        c_count += 1
    elif x =='G':
        g_count += 1

print(a_count,c_count, g_count, t_count)
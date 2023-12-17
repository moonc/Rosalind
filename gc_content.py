
sequences={}
gc_dict ={}
sequence_names =[]

def openFile(filename):
    '''Open a file'''
    f =open(filename)
    return f
    
def splitSequences(gc_file):
    '''Splits sequences by ">" title header symbol'''
    current_sequence=""
    i=0
    j = 0
    count_arr=[]
    

    for y in file2:
        if (y[0] =='>'):
            count_arr.append(y)

    #print(count_arr)

    for x in gc_file:
        x=x.strip("\n")
        #print(x)
        if (x[0] =='>') and (i !=0):
            sequences[sequence_names[len(sequence_names)-1]] = current_sequence
            sequence_names.append(x)
            if len(sequence_names)<len(count_arr):
                current_sequence = ""

        elif (x[0] =='>') and (i ==0):
            sequences.update({x:''})
            sequence_names.append(x)
            i+=1
        else:
            current_sequence = current_sequence+x

    print(sequence_names)
    
    v_seq = sequences[sequence_names[len(sequence_names)-2]]
    val_count=len(v_seq)
    sequences[sequence_names[len(sequence_names)-1]] = current_sequence[val_count:]
    
def calculateGC():
    nucleotides=""
    

    for z in sequence_names:
        a_count = 0
        t_count = 0
        c_count = 0
        g_count = 0
        nucleotides = sequences[z]
        for w in nucleotides:
            if w =='A':
                a_count += 1
            elif w =='T':
                t_count += 1
            elif w =='C':
                c_count += 1
            elif w =='G':
                g_count += 1

        gc_content = round(((g_count+c_count)/(g_count+a_count+t_count+c_count))*100,6)
        gc_dict[z]=gc_content

    


gc_file =  openFile('rosalind_gc.txt')
file2=openFile('rosalind_gc.txt')
splitSequences(gc_file)


calculateGC()
print(gc_dict)


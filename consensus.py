import numpy as np
sequences={}
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

    
    
    v_seq = sequences[sequence_names[len(sequence_names)-2]]
    val_count=len(v_seq)
    sequences[sequence_names[len(sequence_names)-1]] = current_sequence[val_count:]
    
gc_file =  openFile('rosalind_cons.txt')
file2=openFile('rosalind_cons.txt')
splitSequences(gc_file)
big_list = {}#[ [0]*4 for i in range(4)]


def calculateConsensus(sequence_dictionary):
    seq_dict = sequence_dictionary
    counter = 0
    counter_2 = 0
    keys = list(seq_dict.keys())
    key_array_size = len(keys)
    input_size=len(seq_dict[keys[0]])

    small_list = [ [[0]*4]*input_size for i in range(key_array_size)]
    #print(small_list)


    #A is position 0
    #T is position 1
    #C is position 2
    #G is position 3
    s= 0
    for name in seq_dict:
        for nucleotide in seq_dict[name]:
            if nucleotide =='A':
                small_list[counter][counter_2]=[1,0,0,0]
            elif nucleotide =='T':
                small_list[counter][counter_2]=[0,1,0,0]
            elif nucleotide == 'C':
                small_list[counter][counter_2]=[0,0,1,0]
            elif nucleotide == 'G':
                small_list[counter][counter_2]=[0,0,0,1]
            counter_2+=1
        counter+=1
        counter_2 = 0
    small_array = np.array(small_list)
    #print(small_array)

    counting_list = []
    w = 0
    final_sequence  = ""
    
    
    while w<input_size:
        current_array = small_array[:,w]
        ac = 0
        tc = 0
        cc = 0
        gc = 0
        count_list =[]
        for v in current_array:
            if v[0] == 1:
                ac+=1
            elif v[1] == 1:
                tc+=1
            elif v[2] == 1:
                cc+=1
            elif v[3] == 1:
                gc+=1
        
        count_list = [ac,tc,cc,gc]
        counting_list.append(count_list)
        if max(count_list) == ac:
            final_sequence = final_sequence+'A'
        elif max(count_list)== tc:
            final_sequence = final_sequence+'T'
        elif max(count_list)== cc:
            final_sequence = final_sequence+'C'
        elif max(count_list)== gc:
            final_sequence = final_sequence+'G'
        w+=1
        
    print(final_sequence)
    #print(counting_list)

    a_count_list = (np.array(counting_list))[:,0]
    c_count_list = (np.array(counting_list))[:,2]
    g_count_list = (np.array(counting_list))[:,3]
    t_count_list = (np.array(counting_list))[:,1]
    #print(f'A: {a_count_list}')
    #print(f'C: {c_count_list}')
    #print(f'G: {g_count_list}')
    #print(f'T: {t_count_list}')


calculateConsensus(sequences)
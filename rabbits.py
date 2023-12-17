#derived from medium article. Not self code. Adapted from Java.
#https://medium.com/algorithms-for-life/rosalind-walkthrough-rabbits-and-recurrence-relations-4812c0c2ddb3

def rabbitPairs(numMonths,numOffspring):
    if (numMonths == 1): 
        return 1
    
    elif(numMonths == 2):
        return numOffspring

    oneGen = rabbitPairs(numMonths-1, numOffspring)
    twoGen = rabbitPairs(numMonths-2, numOffspring)

    if(numMonths <= 4):
        return (oneGen + twoGen)
    return (oneGen + (twoGen * numOffspring))


pairs = rabbitPairs(34,5)

print(pairs)
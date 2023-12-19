def calculateDominant(k,m,n):
    '''
    Given: Three positive integers k , m , and n , representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
    Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.'''
    size = k+m+n
    dominance = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*size*(size-1))

    return dominance

probability = calculateDominant(25,28,18)
print(probability)

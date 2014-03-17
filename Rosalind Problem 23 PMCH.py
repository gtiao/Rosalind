import math

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def count(string):
    A = string.count('A')
    C = string.count('C')
    T = string.count('U')
    G = string.count('G')
    return A, C, G, T

def perfect_matching(filepath):
    #Parse file
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            string = seq

    counts = count(string)
    return math.factorial(counts[0])*math.factorial(counts[2])

print perfect_matching('/Users/gracetiao/Downloads/rosalind_pmch.txt')


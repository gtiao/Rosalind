import numpy

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
    G = string.count('G')
    T = string.count('T')
    return [A, C, G, T]

def consensus(filepath):
    #Read FASTA file
    FASTA = dict()
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            key = name.strip('>')
            FASTA[key] = seq

    #Create the profile matrix of counts
    n = len(FASTA[key])
    counts = []
    for i in range(n):
        col = ''
        for key in FASTA:
            col = col + FASTA[key][i]
        counts.append(count(col))
    m = numpy.array(counts)
    a = numpy.transpose(m)

    #Evaluate matrix for consensus, and print
    j = numpy.argmax(a, axis=0)
    consensus = ''
    for num in j:
        if num == 0:
            consensus = consensus + 'A'
        elif num == 1:
            consensus = consensus + 'C'
        elif num == 2:
            consensus = consensus + 'G'
        elif num == 3:
            consensus = consensus + 'T'
    print consensus

    #Print profile matrix in specified format
    b = dict()
    b['A'] = a[0]
    b['C'] = a[1]
    b['G'] = a[2]
    b['T'] = a[3]
    for key in b:
        print ':'.join([key, '']),
        for item in b[key]:
            print item,
        print

#consensus('/Users/gtiao/Desktop/Sample_CONS.txt')
consensus('/Users/gtiao/Downloads/rosalind_cons.txt')
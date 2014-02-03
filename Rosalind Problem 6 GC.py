def calculate_GC(string):
    d = dict()
    d['A'] = 0
    d['C'] = 0
    d['G'] = 0
    d['T'] = 0
    for letter in string:
        d[letter] += 1
    tot = sum(d.values())
    GC = float((d['C']+d['G']))/tot
    return GC


def reverse_lookup(d, v):
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)
    return keys


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


def compute_GC_content(filepath):
    FASTA = dict()

    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            key = name.strip('>')
            FASTA[key] = seq

    GC = dict()
    for key in FASTA:
        GC[key] = calculate_GC(FASTA[key])
    GC_vals = GC.values()
    GC_vals.sort()
    max_val = GC_vals[-1]
    out = reverse_lookup(GC, max_val)
    for element in out:
        print element
        print GC[element]*100


compute_GC_content('/Users/gracetiao/Downloads/rosalind_gc.txt')


#read strings in
#make dictionary
#calculate GC content for each key in dictionary, assign as second value in dictionary
#evaluate greatest
#return key with greatest value plus the value
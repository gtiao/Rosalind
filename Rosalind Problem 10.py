#Read fasta file

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


def reverse_lookup(dict, val):
    keys = []
    for k in dict:
        if dict[k] == val:
            keys.append(k)
    return keys



def overlap(filepath, k):
    FASTA = dict()

    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            key = name.strip('>')
            FASTA[key] = seq

    prefix = dict()
    for key in FASTA:
        prefix[key] = FASTA[key][0:k]

    suffix = dict()
    for key in FASTA:
        suffix[key] = FASTA[key][-k:]

    for key in FASTA:
        if reverse_lookup(prefix, suffix[key]):
            for element in reverse_lookup(prefix, suffix[key]):
                if element != key:
                    print key, element


#overlap('/Users/gtiao/Desktop/sample.txt', 3)
overlap('/Users/gtiao/Downloads/rosalind_grph.txt', 3)
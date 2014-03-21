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


def titv_ratio(filepath):
    seqs = []
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            seqs.append(seq)
    seq1 = seqs[0]
    seq2 = seqs[1]

    i = 0
    ti = 0
    tv = 0
    while i < len(seq1):
        if seq1[i] != seq2[i]:
            if (seq1[i] in ['A', 'G'] and seq2[i] in ['C', 'T']) or (seq2[i] in ['A', 'G'] and seq1[i] in ['C', 'T']):
                tv += 1
            else:
                ti += 1
        i += 1
    print float(ti)/float(tv)


titv_ratio('/Users/gtiao/Downloads/rosalind_tran.txt')
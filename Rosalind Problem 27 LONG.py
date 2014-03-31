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

def assemble(filepath):
    reads = dict()
    #Parse file
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            contig = seq #select the last read as the seed contig
            reads[name] = seq

    lengths = [len(seq) for entry in reads]
    half_length = max(lengths)/2

    reads_remaining = len(reads)-1

    #Assemble contig one read at a time
    while reads_remaining > 0:
        match = 'TRUE'

        #Try matching suffix of the contig first
        for i in range(half_length, half_length*2):
            suffix = contig[-i:]
            prefix = dict()
            for entry in reads:
                prefix[entry] = reads[entry][:i]

            if reverse_lookup(prefix, suffix):
                contig += reads[reverse_lookup(prefix, suffix)[0]][i:]
                break
            else:
                match = False

        #If no match, then try matching the prefix of the contig
        if not match:
            for i in range(half_length, half_length*2):
                prefix = contig[:i]
                suffix = dict()
                for entry in reads:
                    suffix[entry] = reads[entry][-i:]

                if reverse_lookup(suffix, prefix):
                    contig = reads[reverse_lookup(suffix, prefix)[0]][:-i] + contig
                    break

        reads_remaining -= 1
    print contig


#assemble('/Users/gracetiao/Desktop/sample.txt')
assemble('/Users/gracetiao/Downloads/rosalind_long.txt')

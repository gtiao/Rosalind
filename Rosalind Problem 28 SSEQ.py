def find_substring_idx(t, s):
    idx=0
    loc=[]
    while idx <= len(s)-len(t):
        if s.find(t, idx) == -1:
            break
        else:
            loc.append(s.find(t, idx)+1)
            idx = s.find(t, idx) + 1
    return loc


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

def lowest_idx(list, floor):
    adjusted = sorted(i for i in list if i > floor)
    return adjusted

def spliced_motif(filepath):
    #Process file
    strings = []
    with open(filepath) as fp:
        seq = read_fasta(fp)
        for name, seq in seq:
            strings.append(seq)
    if len(strings[1]) < len(strings[0]):
        string=strings[0]
        substring=strings[1]
    else:
        string=strings[1]
        substring=strings[0]

    #Find indices of all occurrences of each letter
    idx = dict()
    for letter in substring:
        idx[letter] = find_substring_idx(letter, string)

    #Find a collection of increasing indices
    floor = 0
    motif = []
    for i in range(len(substring)):
        floor = lowest_idx(idx[substring[i]], floor)[0]
        motif.append(floor)
    for i in motif:
        print i,

#spliced_motif('/Users/gtiao/Desktop/sample.txt')
spliced_motif('/Users/gtiao/Downloads/rosalind_sseq.txt')
#Called functions from previous exercises
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

def reverse_lookup_len(dict, l):
    keys = []
    for k in dict:
        if len(dict[k]) == l:
            keys.append(k)
    return keys

def transcribe(string):
    new_word = ''
    index = 0
    while index < len(string):
        if string[index] != 'T':
            new_word = new_word+string[index]
        else:
            new_word = new_word+'U'
        index = index + 1
    return new_word

def translate_RNA(string):
    k = len(string)/3
    i = 0
    prot = ''
    while i < k:
        key = string[3*i:(3*i+3)]
        prot = prot + RNA[key]
        i += 1
    print prot

#Prepare RNA dictionary for protein translation
file = open('/Users/gtiao/Desktop/Rosalind/RNA_codon_table.txt')
RNA = dict()
for line in file:
    pair = line.strip('\n').split(" ")
    key = pair[0]
    RNA[key] = pair[1]


def RNA_splice(filepath):
#Read in strings from FASTA file and create dictionary
    FASTA = dict()
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            key = name.strip('>')
            FASTA[key] = seq

    #Find the longest sequence and set this to the target DNA sequence
    lengths = []
    for key in FASTA:
        lengths = lengths + [len(FASTA[key])]
    m = max(lengths)

    DNA_key = reverse_lookup_len(FASTA, m)
    DNA_seq = FASTA[''.join(DNA_key)]

    #Treat other sequences as introns by successively removing them from target DNA
    for key in FASTA:
        if len(FASTA[key]) != m:
            #excise the intron from the DNA sequence
            DNA_seq = DNA_seq[:DNA_seq.find(FASTA[key])] + DNA_seq[(DNA_seq.find(FASTA[key])+len(FASTA[key])):]

    #For the remaining sequence, perform protein transcription and translation
    RNA_seq = transcribe(DNA_seq)
    translate_RNA(RNA_seq)

RNA_splice('/Users/gtiao/Downloads/rosalind_splc.txt')



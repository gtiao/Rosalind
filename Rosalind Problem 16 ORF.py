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

def reverse_complement(string):
    reverse = string[::-1]
    index = 0
    new_word = ''
    while index < len(reverse):
        if reverse[index] == 'A':
           new_word = new_word + 'T'
        elif reverse[index] == 'T':
           new_word = new_word + 'A'
        elif reverse[index] == 'C':
           new_word = new_word + 'G'
        elif reverse[index] == 'G':
           new_word = new_word + 'C'
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

def substring(t, s):
    idx=0
    loc=[]
    while idx <= len(s)-len(t):
        if s.find(t, idx) == -1:
            break
        else:
            loc.append(s.find(t, idx))
            idx = s.find(t, idx) + 1
    return loc

def translate_RNA(string):
    k = len(string)/3 #This will return the integer part of the quotient
    i = 0
    prot = ''
    while i < k:
        key = string[3*i:(3*i+3)]
        prot = prot + RNA_dict[key]
        i += 1
    return prot

#Prepare RNA dictionary for protein translation
file = open('/Users/gtiao/Desktop/Rosalind/RNA_codon_table.txt')
RNA_dict = dict()
for line in file:
   pair = line.strip('\n').split(" ")
   key = pair[0]
   RNA_dict[key] = pair[1]


def orf(filepath):
    #Read FASTA and set the sequence and reverse complement
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            DNA = seq
    DNA_reverse = reverse_complement(DNA)

    #Transcribe DNA into RNA
    RNA = transcribe(DNA)
    RNA_reverse = transcribe(DNA_reverse)

    #Identify all starts and create dictionaries of the trailing strings; separate dictionaries needed in case of index overlap
    orf = dict()
    orf_reverse = dict()
    idx = substring('AUG', RNA)
    idx_reverse = substring('AUG', RNA_reverse)

    prot = [] #Record all protein strings successfully translated from ORF


    for i in idx:
        orf[i] = RNA[i:]
    for i in orf:
        loc = substring('Stop', translate_RNA(orf[i]))
        if loc: #Consider only strings with 'Stop' codons
            prot.append(translate_RNA(orf[i])[:loc[0]])  #Record the translated protein string only as far as the first 'Stop'

    for j in idx_reverse:
        orf_reverse[j] = RNA_reverse[j:]
    for j in orf_reverse:
        loc = substring('Stop', translate_RNA(orf_reverse[j]))
        if loc:
           prot.append(translate_RNA(orf_reverse[j])[:loc[0]])

    prot = list(set(prot)) #Create a unique (de-dupped) list of the translated protein
    for seq in prot:
        print seq

#orf('/Users/gtiao/Desktop/ORF.txt')
orf('/Users/gtiao/Downloads/rosalind_orf.txt')


#For each letter in the shortest string, do:
#Check all substrings beginning at that letter to see if they are found in the others
#Keep record of the longest substring

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


def check_substr(candidate, strings):
    if len(strings) < 1 and len(candidate) < 1:
        return False
    for i in range(len(strings)): #Check if candidate substring is in *all* strings
        if candidate not in strings[i]:
            return False
    return True

def common_substr(filepath):
    substr='' #Keep a record of the longest common substring

    #Open file and parse strings
    strings = list()
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            strings.append(seq)

    #Find shortest string and walk along this one
    walk=min(strings, key=len)
    for i in range(len(walk)):
        for j in range(len(walk)-i+1):
            if j > len(substr) and check_substr(walk[i:i+j], strings):
                substr = walk[i:i+j]
    return substr

print common_substr('/Users/gracetiao/Downloads/rosalind_lcsm.txt')

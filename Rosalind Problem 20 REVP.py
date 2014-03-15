def return_complement(string):
    if string in ('A', 'C', 'T', 'G'):
        if string == 'A': return 'T'
        elif string == 'C': return 'G'
        elif string == 'T': return 'A'
        elif string == 'G': return 'C'
    else: return None

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

def check_palindrome(string):
    check = True
    i = 0
    while i <= max(range(len(string))[:len(string)/2]):
        if check:
            check = string[i] == return_complement(string[-(i+1)])
            i += 1
        else:
            check = False
            break
    return check


def find_restr_sites(filepath):
    #Open file and parse string
    with open(filepath) as fp:
        for name, seq in read_fasta(fp):
            DNA=seq

    for i in range(len(DNA)):
        #For each letter in the string, create a dictionary of potential palindromic sequences:
        candidates = dict()
        for idx in substring(return_complement(DNA[i]), DNA[i:]):
            if (idx+1)%2 == 0: #cannot be a palindrome if length is odd
                candidates[idx] = DNA[i:][:(idx+1)]

        #Now test to see if each element in the candidates is a palindrome
        for element in candidates:
            if check_palindrome(candidates[element]) and len(candidates[element])>=4 and len(candidates[element])<=12:
                print (i+1), len(candidates[element])

#find_restr_sites('/Users/gracetiao/Downloads/sample.txt')
find_restr_sites('/Users/gracetiao/Downloads/rosalind_revp (1).txt')
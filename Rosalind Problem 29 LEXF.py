def kmers(string, n):
    alph_len=len(string)
    alphabet=dict()

    for i in range(n):
        v = ""
        for j in range(len(string)):
            v = v+string[j]*(alph_len**(n-i-1))
        v = v*(alph_len**i)
        alphabet[i]=v

    output=dict()
    for i in range(alph_len**n):
        entry = ""
        for k in range(n):
            entry = entry+alphabet[k][i]
        print entry

kmers('CMJBFGXPW', 3)
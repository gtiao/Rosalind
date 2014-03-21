def lgis(filepath, increasing):
    with open(filepath) as fp:
        N = int(fp.readline())
        seq = [int(x) for x in fp.readline().split(" ")]

    len_lis = [] #Vector storing length of longest increasing subsequence ending at that position
    prev = [] #Vector storing the position of the preceding value of the subsequence

    for i in range(N):
        len_lis.append(1)
        prev.append(-1)

        for j in range(i):
            if bool(increasing):
                if (len_lis[j] + 1 > len_lis[i]) and seq[j] < seq[i]:
                    len_lis[i] = len_lis[j] + 1
                    prev[i] = j
            else:
                if (len_lis[j] + 1 > len_lis[i]) and seq[j] > seq[i]:
                    len_lis[i] = len_lis[j] + 1
                    prev[i] = j

    idx = len_lis.index(max(len_lis))
    lis = []
    while (idx != -1):
        lis = [seq[idx]] + lis
        idx = prev[idx]

    for x in lis:
        print x,


#lgis('/Users/gtiao/Desktop/sample.txt', 1)
#lgis('/Users/gtiao/Downloads/rosalind_lgis (2).txt', 1)
lgis('/Users/gtiao/Downloads/rosalind_lgis (2).txt', 0)

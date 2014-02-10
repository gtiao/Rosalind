#Key idea: recurrence relation is T_n = T_(n-1) + T_(n-2) - T_(n-(m+1))
#Also: the sequence is identical to the regular Fibonacci sequence up until month m+1, when the rabbits begin to die out

#Ordinary Fibonacci sequence:
def rabbit(n,k):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return rabbit(n-1,k) + k*rabbit(n-2,k)


def mortal_rabbit(n,m):
    if n <= m:
        return rabbit(n,1)
    if n == (m+1):
        return rabbit(n,1)-1
    else:
        #Instead of using a recursive call, which takes too much computing for large numbers and is redundant, record each monthly total
        seq = []
        #Up till month m+1, the monthly totals are identical to the regular Fibonacci sequence
        for i in range(m+1):
            seq = seq + [mortal_rabbit(i+1, m)]
        j = m+1
        #After month m+1, the totals are calculated using the modified recurrent relation
        while j < n:
            seq = seq + [seq[j-1] + seq[j-2] - seq[j-m-1]]
            j = j+1
        #print seq
        print seq[j-1]


mortal_rabbit(96,16)
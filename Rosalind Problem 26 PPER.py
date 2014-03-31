import math

def partial_perm(n,k):
    print (math.factorial(n) / math.factorial(n-k)) % 1000000

partial_perm(94, 10)
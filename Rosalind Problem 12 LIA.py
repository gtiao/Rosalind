from scipy.stats import binom

def alleles(k, N):
    prob = binom.sf(N-1, 2**k, .25, loc=0) #1-cdf, where cdf is P<=quantile
    print prob

#alleles(2, 1)
alleles(6, 18)
def mendel(k, m, n):
    k=float(k)
    m=float(m)
    n=float(n)
    N=float(k+m+n)
    p=((2*k*(m+n)+m*n+k*(k-1))/(N*(N-1))+(3*m*(m-1))/(4*N*(N-1)))
    print p

#mendel(2,2,2)
mendel(19,16,30)
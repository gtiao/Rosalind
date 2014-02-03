import math

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]): #this is the inductive (recursive) step
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
                #move the first element (element[0:1]) along each position in each permutation of one size smaller


def gene_order(len):
    print math.factorial(len)
    elements = [x+1 for x in range(len)]
    perms = all_perms(elements)
    for element in perms:
        for item in element:
            print item,
        print

gene_order(6)
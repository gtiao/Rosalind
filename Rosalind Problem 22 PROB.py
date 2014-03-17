import math

def count(string):
    A = string.count('A')
    C = string.count('C')
    T = string.count('T')
    G = string.count('G')
    return A, C, G, T


def generate_log_probs(n):
    if n < 0 or n > 1:
        print 'GC content is not a valid fraction.'
    G = math.log10(n/2)
    C = math.log10(n/2)
    T = math.log10((1-n)/2)
    A = math.log10((1-n)/2)
    return A, C, G, T

def random_string(filepath):
    #Parse file
    with open(filepath) as fp:
        string = fp.readline()
        array = [float(x) for x in fp.readline().split(" ")]

    string_count = count(string)

    output = []
    for item in array:
        probs = generate_log_probs(item)
        output.append(string_count[1]*probs[1]+string_count[2]*probs[2]+string_count[3]*probs[3]+string_count[0]*probs[0])
    for y in output:
        print round(y, 3),

random_string('/Users/gracetiao/Downloads/rosalind_prob.txt')
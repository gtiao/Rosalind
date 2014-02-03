def all_perms(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for p in all_perms(s[:i] + s[i+1:]):
                yield s[i] + p

for element in all_perms('ABCD'):
    print element

#s='ABC'
#range(len(s)) = [0,1,2]


#for i=0
#s[:i] = ''
#s[i+1:] = 'BC'
#inductive step: assume all_perms('BC') = 'BC' and 'CB'
#yield: ABC, ACB

#for i=1
#s[:i] = 'A'
#s[i+1:] = 'C'
#inductive step: assume all_perms('AC') = 'AC' and 'CA'
#yield: BAC, BCA

#for i=2
#s[:i] = 'AB'
#s[i+1:] = ''
#inductive step: assume all_perms('AB') = 'AB' and 'BA'
#yield: CAB, CBA
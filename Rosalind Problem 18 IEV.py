#Take integer vector, process
#Feed into equation

def iev(string):
    couples = [int(x) for x in string.split(" ")]
    E = 2*(couples[0] + couples[1] + couples[2] + .75*couples[3] + .5*couples[4])
    print E


#iev('1 0 0 1 0 0 1')
iev('18674 17603 19609 18284 18252 19829')
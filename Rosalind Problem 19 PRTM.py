#Create mass dictionary
file = open('/Users/gtiao/Desktop/Rosalind/Monoisotopic_mass_table.txt')
mass = dict()
for line in file:
   pair = line.strip('\n').split(" ")
   key = pair[0]
   mass[key] = pair[1]

def weight(string):
    m = 0
    for x in string:
        m += float(mass[x])
    print m


#weight('SKADYEK')
weight('EGFMWELHMNHKHMPVPQIYQWRHTWCWHMIQGVYSTRSYPTSLINGEWFDIKWSGNFQWKSRRPSRGMSDQGATHCLPDEPELWCFTMGDACWIIAEQEDDALYGCYATGCEFKCGIILTWMCYYWPFCSSKQYHWMIRKHSIDKIIYHGSAHVAMEELHTHGTNTCPGYVCPGRYVIEICDVPCNTYEPSFHEVGPSIMSTNVIVNGFKARKDCDMQWAPNALQKRIKAFQTYQGYWPTSWRNVSKKWLSTIAHIMIETLGPKIGTIRMKSIGISRNTLCIMNLHQVSHRNRMLDMFTVVAGIWVLKCECGKSVKYATVDVQWPGSLFPAKPTRAYCSAKIHQNRTQFPCVHNRCCMRPNRDCKQTQNVNGFNHVMHVDLDLICRDTKFCGTSSNEWIHTLELTWAFHDMWWHAHDHSSGGVVNDKSLKWNIMADECFRLFALHPQLNWTFFRMPGNVLRIVVASRICPFNCKPCTGIDVHNDVFTPTHEHREMPEHKEKQATIKLTFSGQKFKITQWVYFYMSPLVWSVDAILNEDGAKANMHDVCTWRHPMVELDRHNVTKYEMFCSSAETIMNRHGRLQPCFAMWGGSQYREMGVQEFCQMSGNHCNRQFHLARMRYFICTDDVAHVAIIWQEAQNELPRKPWSWGIWRSHGDKKYPCIEKDVTQQHLKWMELSNRCTTSNTKVQNKHWVLLIMQPAIIPHCLYGTTWDDFYEEFPCGDWDITPKYMQDYQMEYFCHKHQRRMLEGHIWCEKYIHESYGVWKIICQVWYPMMYLERWTSYQMRVKGSYFHYRQEQLCHCKT')
def reverse_lookup(dict, val):
    keys = []
    for k in dict:
        if dict[k] == val:
            keys.append(k)
    return keys

#Prepare RNA dictionary for protein translation
file = open('/Users/gtiao/Desktop/Rosalind/RNA_codon_table.txt')
RNA_dict = dict()
for line in file:
   pair = line.strip('\n').split(" ")
   key = pair[0]
   RNA_dict[key] = pair[1]

def mrna(string):
    #Create list of each protein in string, including 'Stop'
    AA = list(string)
    AA.append('Stop')

    #Create corresponding list that counts the number of codons that could encode that protein
    AA_count = []
    for item in AA:
        AA_count.append(len(reverse_lookup(RNA_dict, item)))

    #Now multiply out the count list to give the total number of strings that could encode the entire protein sequence
    #Note that at each codon, the total, m, is reduced modulo 1000000
    m = 1
    for element in AA_count:
        if m > 1000000:
            m = m % 1000000
        m = m * element
    print m % 1000000

#mrna('MA')
mrna('MAAVYNTNKYPSWWGEFYSAQMNPNACVEQGTMEMWAASTVIHAAAADALFSLYFMTAVFRYQVHIMQWTLWSKNCPTLSWKAYNLGNNVWLYQPQQTIMLHPGGEPFGPMPDAKSTEWDQQEMGISIKEYDYCSYKHKYYIAGMGPKFKWIMFMRDSIFAQWKGGYESIFPIICMDYQNATGWNIGPIPTSMDSGIFPLSHGYQLDLCCATNKTDEDAPKVLWGFATRLSRNIRHDRGPDNQPQLHHAMMHLYRPLICDVATRHGAVIHPTEHPFGGTQGQGSHHNIPKKMWMYVACKMKSTEIGCMAVIYGQGIRKWFFKGQLRVNHNIMYATWDSIINREGFCARYEVVLGHTVANEDADGICHKVRWMPIDIYEKCFDPVWPPHCEGQWDVYQESTSNKSEDHQFVVECPEQDKYKNIKLFFNDTVMQHPLWWQPADPDCVLLRYNYGTNAFEKHEWYRWALDWADHCNTGRMMYNNHWVDTYVMHTVKNMSMSRKGHMEMRGMVYWGTAEPDRASVLSHFIGSVNITWREKQGFISEQWFDCKMECDGWEIKLMMGFWATVACASYHVTVLACKCYKQCWQIPMNCAASHLYISNIWEPSHKASGECNDALPQLSRIVWKCCEKCGCSEYPNQNPCWFRRQPERAWAASMERDLKFFRTLGVQVSHNKNKTGREKLVRSDKLVWAVNHMYELNVDCFYYHHCYDCAQWGWYRSFTFYRFHSPYACGPWTTKDVFNAAIEQHDWLKSHHVYRGRAPHKFLKPKYPSWAWYRFTEHLFTENVNSSRSEYGCQRTLEMIHDMCHGYRHDGDLVMSSNVCVCHSWFATSARGKLMAWNQPYTASFIKTWFMRLSLRGNVFTDWHRARIWCYSHEPVMLQYVWILWNCKSWLESMDKEMWMDVHECYLWRIRAWCSFKDKSVLLLREWMWFQPNMLDRRGLDQWVVLNIQFRFNRCAQYMWGTMKWPMESMDLLIMISNHMNRGKEDYIKAGWGAIF')
def hamm(s,t):
    i = 0
    d = 0
    while i < len(s):
        if s[i] != t[i]:
            d += 1
        i +=1
    print d

#hamm('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')

hamm('TGGCGTACAGTATATTAGTTAGTAACTTGTGAAGTACACTTCTAAATGCATCTCACCGGGTTATGTCCCGGCCGACAGAGATACAGGTAGGGAACAGGGAGCCTACCGAAGTCTATTTCCCGATCAATTTTTGTGGGGCGTTCTCGCAGAGGGAAGCATCACACACGTTCGCAATTCCCCGGGACTAACCCATCTATCTGCGGACACTGTAATCTTGATAGCATGAACTTCAGCCATGAGATGTTAGCTGACCTAAGCTTCCATAGATCTTAACACGTTATTCATGCAACATAGTATACTAAAATCGTCGAATCAGTTCAGTTCGTCTGACAGGTCCCGTCTAACGCGTTGAAGTTTATATTGGCACTGAGCCAAGTTTGGCGCATCATTTGATATATCCAAATCCAGGTAGATCCGTGACTGTTCCAACGACCATCGGTCGTCGGCTTGTTCCCCTGGGAGTTAGTTATCTCGCGAGTCCTTCCCGCAGAAAGTTCCACATCTGCATGGGCGTCCTACGATCTTCAGAAGGTCTCTTATTCCCTGAAGGCACGGTAAGGTCGACGTGCGATTGTACACACAGGCGGTCACGAGCTCCAGAAACTCCCGTATACAGGGCTTGGTCCACAGCTAACCAGACCAACCGATATCGAGAGTAACAAGCTACTGCAGCTAAGACAGAAACCAAAAATTAACTTCCAGTGTCGGATGAGTAGGGCGAATAACCTGCGGAGAGAGCTGAAGCAAATGGCTTCAGTATATCTACCTCACTCGCCCAGAACCGATTAATTGCCGATGACATGCCTCAAGGGGAGTCGTGCTAAGATAAACCTGTAGGTGAATAAATTTCAATCCCGAGCAACTGCTTATTTCTTCGGTCTCGTGGTTAGAAGCGATTATGACAGTCGCAGCCCTGGTATAGAGAGATATGAGGGCAATAGGGAGTCCAGCGCC', 'ACGTCGGCAACATACCAGCTGATACTACATAGAGGAGTTGCCTCAAAGCCCGTGATTCGTTTATCGTACGTCCTGGTCGGACGGACAATCAACATTAAGACCCTTTCACACCTCTTTAAGCTAACAGATTGTCCGCGGCCATCGACCCGAGTAAAGTAACACGAGAGTTCGCCGCCCTCCGTAAGTTTGGTAACTATTGGCGTACACCGGCCGCCTGGGAGCAGGTATTTTCCCTGGGCGATCTTATCTGTACTGCGATACCATATGGTTTGGCCAATAACAAATCTGCCACTTAATACTCGGGTCGTCGTGTAAGATCAGACCTTGCGCCAGCTAAAGTCTAACACGTTGTATCTCTTGTTGGGAGTTAGCCTAGCTGCGCTACTCAATGGGTAGATACAACTACATGAGGAGGCGTCACTCGTCCAACGACCAGAACGGTGCAGCAGATCCCCCCGAGAGTTACGTATTTATCGTGTCGTTCCAGCAGATGAATCGCCAGATGTTTCAGTGTACTCAAGCCTCCCGAAAATATCTAAAACCCGTATTGCACAGAACGATCGAGACGCGCTCACAAACAAAGGTAGTTCGAAGGTGTCGACAGTCCTCGAGAAAAGTCTTGCTGCGGCTCTTACCCACCTGTTTGGTACCGAAAGTATCATCTTAGTGTACCCGTTTTAATAATCATAAGTAAGGTTCCCGGGAGTGCACAGAGGGGCCGATCCCCTAACGAGGGACCCGATGCAATTGGTTACTGCAAACGTAGGTACTGCTCGGCTTATGGCTAAGCCGCACGTTTAGGACCTCCTGCGTCTTTTGTCTGCGGTTTATCCGCGGGTCACGATATTTGAAAACGCGGCAATAGCCAAATTTCCCCTACAAGAGCTTTGAGCAGATGCCCACAGAATCAGCCCTCTTTTGGGAAGAGCTGATCACCGTCATGAGCTATTGGGA')
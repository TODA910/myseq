import re

# SeqCal module
def gcContent(seq):
    '''To calculate G+C/(A+T+G+C)''' 
    return (countBase(seq, 'G') + countBase(seq, 'C'))/len(seq)

def countBase(seq, base):
    '''Count specific base in the input sequence''' 
    return seq.count(base.upper())

def countBasesDict(seq):
    '''Count number of each base'''
    basesM = {}
    for base in seq:
        basesM[base] = basesM.get(base, 0)+1
    return basesM


# SeqPattern module
def cpgSearch(seq):
    '''Search CpG motif in the input sequence'''
    cpgs = []
    for m in re.finditer('CG', seq, re.I):
        cpgs.append((m.group(), m.start(), m.end()))
    return cpgs

# Input
seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
seq = seq.upper()
print("Count A Bases: ", countBase(seq, 'A'))
print("GC Content:", gcContent(seq))
print("Search CpG: ", cpgSearch(seq))

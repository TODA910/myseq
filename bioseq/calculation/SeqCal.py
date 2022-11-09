
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

# print("in bioseq.calculation.SeqCal.py")
if __name__ == '__main__':
    seq = 'TCAGGGCTAAAGCGCATCCTAC'
    print("test: Count specific base:", countBase(seq, "A"))
    print("test: GC Content:", gcContent(seq))
    print("test: Count Bases: ", countBasesDict(seq))



def addDict(dic1, dic2):
    typeDict = dict(list=addSeq, tuple = addTuple, str = addSeq, set = addSet, int = addSeq, dict = addDic)
    t1 = type(dic1)
    t2 = type(dic2)
    t1 = str(t1)
    t1 = t1[8:-2]
    t2 = str(t2)
    t2 = t2[8:-2]
##    print(t1)
##    print(t2)
##    print(t1==t2)
    if t1 == t2 and t1 in typeDict:
##        print(typeDict[t1])
        return typeDict[t1](dic1, dic2)

def addSeq(seq1, seq2):
    return seq1 + seq2

def addTuple(tuple1, tuple2):
    return tuple(list(tuple1) + list(tuple2))

def addSet(set1, set2):
    return set(list(set1) + list(set2))

def addDic(dic1, dic2):
    for (k, v) in dic1.items():
        dic2[k] = v
    return dic2
    

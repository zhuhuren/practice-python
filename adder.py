def adder(**kargs):
    if len(kargs)>=1:
        L = []
        for v in kargs.values():
            L.append(v)
        result = L.pop()
        for x in L:
            if type(x) == type(result):
                result += x
            else:
                print('TypeError')
                break
        else: return result

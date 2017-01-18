from random import randint
from string import ascii_lowercase, capwords
for h in range(randint(7,15)):
    para = []
    for i in range(randint(30,150)):
            word = ''
            for j in range(randint(2,9)):
                    k = randint(0,25)
                    word += ascii_lowercase[k]
            para.append(word)
    ins_loc = 0
    while ins_loc + 1 < len(para):
        para[0] = capwords(para[0])
        ins_loc += randint(3, 10)
        if ins_loc + 1 < len(para):
            para[ins_loc] += ','
        ins_loc += randint(3, 10)
        if ins_loc + 1 < len(para):
            para[ins_loc] += '.'
        if ins_loc + 1 < len(para):
            para[ins_loc + 1] = capwords(para[ins_loc + 1])
##    para.append('.')
##    print(para)
    print(' '.join(para) + '.')


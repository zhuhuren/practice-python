file = open('maze.txt', 'r')
L = []
for line in file:
    print(line)
    subL= []
    for ch in line[:-1]:
        subL.append(ch)
    L.append(subL)
file.close()
print(L)
for x in L:
    print(x)

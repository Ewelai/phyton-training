treeSize = int(input('Enter tree size: '))

for i in range(treeSize):
    print(' ' * (treeSize - i -1) + '*' * (i * 2 + 1))
    
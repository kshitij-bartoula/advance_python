from itertools import permutations
for item in permutations('WXYZ', 2):
    print(''.join(item))

#WX
#WY
#WZ
#XW
#XY
#XZ
#YW
#YX
#YZ
#ZW
#ZX
#ZY
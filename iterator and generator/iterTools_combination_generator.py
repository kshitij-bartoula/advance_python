from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product
print (list(combinations('WXYZ', 3)))
#[('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]

for item in combinations('WXYZ', 2):
    print(''.join(item))

#WX
#WY
#WZ
#XY
#XZ
#YZ
#combinations_with_replacement contains xx ww yy zz also
for item in combinations_with_replacement('WXYZ', 2):
    print(''.join(item))

#WW
#WX
#WY
#WZ
#XX
#XY
#XZ
#YY
#YZ
#ZZ

arrays = [(-1,1), (-3,3), (-5,5)]
cp = list(product(*arrays))
print (cp)
#[(-1, -3, -5),
# (-1, -3, 5),
# (-1, 3, -5),
# (-1, 3, 5),
# (1, -3, -5),
# (1, -3, 5),
# (1, 3, -5),
# (1, 3, 5)]
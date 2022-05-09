from collections import Counter
print (Counter('superfluous'))
#Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})

counter = Counter('superfluous')
print (counter['u'])
#3
print (list(counter.elements()))
#['u', 'u', 'u', 'o', 'p', 'e', 'f', 'l', 'r', 's', 's']
print( counter.most_common(2))
#[('u', 3), ('s', 2)]


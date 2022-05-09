d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print (d)
#{'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}

keys = d.keys()
print (keys)
#dict_keys(['apple', 'orange', 'banana', 'pear'])

keys = sorted(keys)
print (keys)
#['apple', 'banana', 'orange', 'pear']

for key in keys:
    print (key, d[key])

#apple 4
#banana 3
#orange 2
#pear 1


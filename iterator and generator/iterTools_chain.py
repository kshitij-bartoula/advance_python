from itertools import chain
my_list = [['foo', 'bar']]
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list = list(chain(my_list, cmd, numbers))

print (my_list)
#['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]
# extend() supports only one arg so ta add multiple list we can use chain

#alternate
my_list = ['foo', 'bar']
my_list += cmd + numbers
print (my_list)
#['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]
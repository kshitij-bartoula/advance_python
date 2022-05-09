from itertools import repeat
repeat(5, 5)
repeat(5, 5)

iterator = repeat(5, 5)
print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 21, in <module>
# print (next(iterator))
#StopIteration:
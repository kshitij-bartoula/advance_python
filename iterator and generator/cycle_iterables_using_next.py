from itertools import cycle
polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)
print (next(iterator))
#'triangle'

print (next(iterator))
#'square'

print (next(iterator))
#'pentagon'

print (next(iterator))
#'rectangle'

print (next(iterator))
#'triangle'

print (next(iterator))
#'square'
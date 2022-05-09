from itertools import accumulate
import operator
print (list(accumulate(range(1, 5), operator.mul)))
#[1, 2, 6, 24]
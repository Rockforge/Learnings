import itertools
import functools


l = [1, 2, 3, 4, 5]
result = itertools.accumulate(l)


fresult = functools.reduce(lambda x, y: x+y, l)
print(fresult)
print(list(result))

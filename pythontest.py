import numpy 
import random
# s = np.random.randint(0, 20, random.randint(0, 20))
# t = random.randint(0, 20)
s = numpy.random.randint(0, 5, random.randint(0, 5 - 1))
t = [tuple(x) for x in numpy.random.randint(0, 5, size=(random.randint(0, 15), 2))]
lst = []
lst.append('a')
lst.append('b')
lst.append('c')
lst.append('d')
lst.append('e')
lst.append('f')
lst.append('g')
lst.append('h')

lst.pop(random.randint(0, len(lst) - 1))
print(lst)

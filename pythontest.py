import numpy 
import random
# s = np.random.randint(0, 20, random.randint(0, 20))
# t = random.randint(0, 20)
s = numpy.random.randint(0, 5, random.randint(0, 5 - 1))
t = [tuple(x) for x in numpy.random.randint(0, 5, size=(random.randint(0, 15), 2))]
lst = []
lst.append('Hi')
lst = set(lst)
lst[4] = 'Hello'
print(lst)
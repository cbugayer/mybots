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
rand = numpy.random.randint(random.randint(0, 40), size=(1, random.randint(0, 40)))
# rand = random.sample(range(100), random.randint(100, 110))
a = numpy.array([[1, 2], [3, 4]])
b = numpy.random.random(2)

a = [[-0.873272,   -0.14136105,  0.02987473],
 [-0.04551776, -0.20933988, -0.70261167]] 
b = [numpy.array([0.51581855, 0.92757324, 0.72459052])]
print(numpy.concatenate((a, b), axis=0))



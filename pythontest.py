import numpy 
import random
# s = np.random.randint(0, 20, random.randint(0, 20))
# t = random.randint(0, 20)
s = numpy.random.randint(0, 5, random.randint(0, 5 - 1))
t = [tuple(x) for x in numpy.random.randint(0, 5, size=(random.randint(0, 15), 2))]
lst = []
for i in range(0, random.randint(1,18)):
    lst.append((random.randint(-10,0),random.randint(0, 6)))
z = numpy.random.rand(3,4,5)
# print(t)
print(str("hi"))
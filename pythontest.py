import numpy 
import random
import numpy as np
import matplotlib.pyplot as plt
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
# rand = numpy.random.randint(random.randint(0, 40), size=(1, random.randint(0, 40)))
# rand = random.sample(range(100), random.randint(100, 110))
a = numpy.array([[1, 2], [3, 4]])
b = numpy.random.random(2)

a = [[-0.873272,   -0.14136105,  0.02987473],
 [-0.04551776, -0.20933988, -0.70261167]] 
b = [numpy.array([0.51581855, 0.92757324, 0.72459052])]
# print(numpy.concatenate((a, b), axis=0))
# print(random.randint(0,-1))
# print(numpy.arange(0,5))
arr =  [3.9407799878576038, 2.188009999206728, 3.7948106937851973, 1.1471551691629895, 2.9749107937588546, 2.5865814746900804, 1.6417161535369764, 3.601328718956459, 3.1171719146488326, 2.786486968568812, 3.3827776651840873, 4.373091280524167, 2.929431011588746, 1.6626257987121504, 4.062346020821686, 3.1912468883954994, 2.802902857617823, 2.096640207863991, 4.487763926512492, 2.9838387811591187, 3.3191359195400105, 3.656528723521788, 3.3350937650171426, 1.5655928864190547, 1.9414877875542096, 4.999025418647941, 4.219178926172593, 3.4842614689904847, 3.645867382979635, 4.428274885298484, 2.726272095363814, 3.312529529679004, 3.039809341154429, 1.6626304561992677, 3.272499825261107, 4.625142933641982, 2.1384075342533975, 2.4528442648156554, 3.474567944903107, 1.8062974366313835, 2.5685160165712717, 2.3420643491942594, 0.41707796512839823, 2.5769610253897692, 4.66484338590583, 3.849920733209582, 3.7559059556693932, 2.5051867382359285, 4.343590320755141, 2.9614060906759527, 3.035060452127593]
maxes = []
for i in range(len(arr)):
    maxes.append(max(arr[:i+1]))
print(list(set(maxes)))
# Create random subplots


# fig, ax = plt.subplots()
# p = ax.plot(numpy.arange(0, len(arr)), arr)

# f = plt.figure(figsize=(10, 10))

# f.add_subplot(2,2,1)

# f.add_subplot(2,2,2) 
# f.add_subplot(2,2,3)
# f.add_subplot(2,2,4)
# fig.add_subplot(2,2,1)
# plt.plot(numpy.arange(0, len(arr)), arr)
# fig.add_subplot(2,2,2)
# plt.plot(numpy.arange(0, len(arr)), maxes)
# fig.add_subplot(2,2,3)
# plt.plot(numpy.arange(0, len(arr)), arr)
# fig.add_subplot(2,2,4)
# # plt.plot(numpy.arange(0, len(arr)), maxes)
# fig1 = plt.figure(figsize=(10, 10))
# plt.plot(numpy.arange(0, len(arr)), arr)
# fig2 =plt.figure()
# plt.plot(numpy.arange(0, len(arr)), maxes)
# fig3 = plt.figure()
# plt.plot(numpy.arange(0, len(arr)), arr)
# fig4 = plt.figure()
# plt.plot(numpy.arange(0, len(arr)), maxes)

# # plt.plot(numpy.arange(0, len(arr)), arr
# # plt.show()
# # Save all plots in a list
# plots = [fig1, fig2, fig3, fig4]
# x = [[numpy.arange(0, len(arr)),numpy.arange(0, len(arr))],[numpy.arange(0, len(arr)),numpy.arange(0, len(arr))]]

# y = [[maxes,arr],[maxes,arr]]
# plots = np.reshape(plots, (2,2))
# print(plots)
# fig, ((ax0, ax2), (ax1, ax3)) = plt.subplots(2,2)
# for i, p in enumerate(plots):
#     'ax'+str(i) = p
# for i, ax in enumerate(fig.get_axes()):
#     ax = plt.subplot(2,2,i+1)
# fig.show()
# for i, p in enumerate(plots):
#     ax0 = 




# for i, ax in enumerate(axes):
#     ax[i].plot(x[i][0], y[i][0])
# for p in plots:
#     p.show()
    

# plt.show(fig)

# f = plt.subplot(2,2,1)
# f.axes.append(plots[0])
# f.axes.append(plots[1])
# f.axes.append(plots[2])
# f.axes.append(plots[3])
# plt.show(f)

# fig1, ax = plt.subplots(2, 2, sharex=True, sharey=True)
# ax[0, 0].plot(range(10))

# fig2 = plt.figure()
# fig2.axes.append(ax)


# plt.show()

# fig = plt.figure()

# plt.subplot(2, 2, 1)


# plt.subplot(2, 2, 2)
# plots[1].get_axes()

# plt.subplot(2, 2, 3)
# plots[2].get_axes()

# plt.subplot(2, 2, 4)
# plots[3].get_axes()

# plt.show()

class PYTEST:

    def __init__(self):

        self.lst = []



    def add_plot(self, plot):

        self.lst.append(plot)

    def make_plots(self):

        fig = plt.figure(figsize=(10, 10))

        plt.plot(numpy.arange(0, len(arr)), arr)
        
        return fig
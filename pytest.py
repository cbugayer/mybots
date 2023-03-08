from pythontest import PYTEST
import matplotlib.pyplot as plt
lst = []
p = PYTEST()
plot = p.make_plots()
plot2 = p.make_plots()
plot3 = p.make_plots()
plot4 = p.make_plots()
lst.append(plot)
lst.append(plot2)
lst.append(plot3)
lst.append(plot4)
for plote in lst:
    fig = plt.figure()
    fig.axes.append(plote)
    plt.show()

# plt.show(fig)




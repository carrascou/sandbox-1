from random import uniform
rannumlist = []
for i in range(1, 100):
    rannum = uniform(0.0, 10.0)
    rannumlist.append(rannum)
print(rannumlist)
ranfile = open("randomGenNums.txt", "a")
ranfile.write(str(rannumlist))
ranfile.close()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
# ax.plot(t, s)
ax.plot(rannumlist)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')

ax.set(xlabel='Samples', ylabel='Random',
       title='Random numbers generated between 0.0 to 10.0')

ax.grid()

fig.savefig("test.png")
plt.show()
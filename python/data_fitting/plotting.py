#!/usr/bin/python3

# run these commands in the shell to get a feel for plotting
# see here for more documentation:
# "http://matplotlib.org/users/pyplot_tutorial.html"

import numpy as np
import matplotlib.pyplot as plt

# creates range of points for dependent variable
# np.linspace(start, end, number of points)
x = np.linspace(0, 20, 50)

# can put any function that can handle arrays as second argument
plt.plot(x, np.sin(x),'bo')
plt.plot(x, np.sin(x),'k')

# make it pretty!!
plt.xlabel('x-label (units)', fontsize = 14)
plt.ylabel('y-label (units)', fontsize = 14)
plt.title('My Fancy Graph', fontsize = 20)

# start strings with "r" for raw string to interpret latex
# first numbers are location of text on graph
plt.text(10, -1.1, r'$\rho = \frac{1}{\mu}$', fontsize = 16)

# define ranges for axis
plt.xlim(-1,22)
plt.ylim(-1.5,1.5)

#plt.errorbar(x, y, fmt = 'ro', xerr = xe, yerr = ye)

plt.show()
plt.savefig(f.__name__+'_plot.pdf', bbox_inches=0, dpi=600)

# need to clear figure if we're going to make another graph in same program
plt.clf()

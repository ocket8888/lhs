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

plt.xlim(-1,22) # x-axis range
plt.ylim(-1.5,1.5) # y-axis range

plt.show()
#plt.errorbar(x, y, fmt = 'ro', xerr = xe, yerr = ye)

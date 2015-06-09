#!/usr/bin/python3

# Needed Modules
# ================

import numpy as np
import matplotlib.pyplot as plt
import scipy.odr.odrpack as odrpack
import sys

# documentation for the odrpack library can be found here:
# "http://docs.scipy.org/doc/scipy/reference/odr.html#id1"

# Functions to fit
# ================

# elements of B are the free parameters for fitting

def fsin(B,x):
    return B[0]*np.sin(B[1]*x)

def fexp(B,x):
    return B[0]*np.exp(B[1]*x) + B[2]

def fpoly(B,x):
    return B[0]*(x**3) + B[1]*(x**2) + B[2]*(x) + B[3]

# Import data
# ===========

def import_from_csv(data_file):

    x = []
    x_err = []
    y = []
    y_err = []

    with open(data_file, "r") as f:

        # need to remove newlines and commas (for CSVs)
        data = np.array([line.rstrip().split(", ") for line in f])

    # if len 4, assume data in [x, x_err, y, y_err] format
    # otherwise transpose
    # in general, nested if statements are terrible, don't do this
    if len(data) != 4:
        data = np.transpose(data)
        if len(data) != 4:
            print("data not in correct format")
            sys.exit()

    # cast to float for computation (copies array)
    try:
        data = data.astype(float)

    # delete first line (optional, only do this to get rid of headers)
    except:
        data = np.array([row[1:] for row in data])
        data = data.astype(float)

    x = data[0]
    x_err = data[1]
    y = data[2]
    y_err = data[3]


    return x, x_err, y, y_err

# Do fit
# ======

# perform orthogonal distance regression for given model f
def do_odr(f, x, xe, y, ye, estimates):

    model = odrpack.Model(f)

    # sx and sy should be the covariances
    data = odrpack.RealData(x, y, sx=xe, sy=ye)

    # need to hard-code in estimates for parameters
    odr = odrpack.ODR(data, model, estimates)

    output = odr.run()

    return output

# Plot - requires matplotlib
# --------------------------

def plot_fit(x, xe, y, ye, f, betas):

    plt.xlabel('x-label (units)', fontsize = 14) # x-axis label
    plt.ylabel('y-label (units)', fontsize = 14) # y-axis label
    space = 0.1 # desired space as fraction of respective ranges

    xspan = x.max() - x.min() # range of x values
    yspan = y.max() - y.min() # range of y values
    xspace = space * xspan # space on either side of x min/max
    yspace = space * yspan # space on either side of y min/max

    plt.xlim(x.min()-xspace,x.max()+xspace) # x-axis range
    plt.ylim(y.min()-yspace,y.max()+yspace) # y-axis range

    plt.errorbar(x, y, fmt = 'ro', xerr = xe, yerr = ye) # data and error bars

    modelx = np.linspace(x.min()-xspace, x.max()+xspace, 500)

    plt.plot(modelx, f(betas, modelx))

    # save plot to pdf
    plt.savefig(f.__name__+'_plot.pdf', bbox_inches=0, dpi=600)

    # on screen display of plot
    #plt.show()

    # clear figure, so we'll make separate plots for each fit
    plt.clf()

# Analyze Fit
# -----------

# look under "regression analysis" on this link for definition:
# "https://en.wikipedia.org/wiki/Goodness_of_fit"

def chi2(x, xe, y, ye, model, betas):

    # Chi^2 Calculation
    chi2 = 0.
    for i in range(len(y)):
        residual = y[i] - model(betas, x[i])
        sigma = (xe[i]**2. + ye[i]**2.)**0.5
        chi2 += (residual / sigma)**2.

    # Reduced Chi^2 Calculation
    dof = len(y) - 1 - len(betas) # Degrees of freedom (points - parameters in fit)
    reduced_chi2 = chi2 / dof # Reduced chi^2 (chi^2 / degrees of freedom)

    print ('Degrees of Freedom:', dof)
    print ('Chi-Square:', chi2)
    print ('Reduced Chi-Square:', reduced_chi2)

# Run file
# --------

# need to run with data file as 1st argument
# prints output and shows plot

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Need to supply input file as first argument")

    data_file = sys.argv[1]
    x, xe, y, ye = import_from_csv(data_file)

    # define functions we want to fit to, and initial parameter guesses
    fits = [fsin, fexp, fpoly]

    sine_est = [5.0,0.5]
    exp_est = [2000.0,-0.2, 100.0]
    poly_est = [1.0, 1.0, 1.0, 1.0]
    ests = [sine_est, exp_est, poly_est]

    # see what a difference your initial estimates make!
    #ests = [[1.0,1.0],[1.0,1.0],[1.0, 1.0, 1.0, 1.0]]

    # do fit with all options, print results
    for (fit, est) in zip(fits, ests):

        result = do_odr(fit, x, xe, y, ye, est)

        print("Results for",fit.__name__,":")

        print("Estimated Parameters:", result.beta)
        print("Parameter Standard Errors:", result.sd_beta)
        print("Sum of Square Errors:", result.sum_square)

        plot_fit(x, xe, y, ye, fit, result.beta)
        chi2(x, xe, y, ye, fit, result.beta)
        print('\n')

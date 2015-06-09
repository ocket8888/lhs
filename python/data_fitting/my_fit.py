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

def fpoly(B,x):

# Import data
# ===========

def import_from_csv(data_file):

    with open(data_file, "r") as f:

        data = f

    return x, xe, y, ye


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

# use plotting.py as a reference

def plot_fit(x, xe, y, ye, f, betas):

    plt.show()


# Analyze Fit
# -----------

# look under "regression analysis" on this link for definition:
# "https://en.wikipedia.org/wiki/Goodness_of_fit"

def chi2(x, xe, y, ye, f, betas):

    print ('Degrees of Freedom:', dof)
    print ('Chi-Square:', chi2)
    print ('Reduced Chi-Square:', reduced_chi2)

# Run file
# --------

# This needs to:
# - get filename as first command-line argument
# - import data from file into x, xe, y, ye variables
# - define a list of models to try fitting to the data
# - define initial guesses for the fit parameters
# - run "do_odr" for all the models and parameters
# - calculate chi squared for each model
# - plot each fit
# - return results (print or save to file)

if __name__ == "__main__":

import math

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x +b
    #return a*x+b

#Experimental x and y data points
xData = np.array([0.500, 1.000, 1.500,2.000,2.500,3.000,3.500,4.000,4.500]) #t in ms
yData = np.array([485,273,163,89.8,50.8,33.8,12.8,11.3,4.5]) #y in mV

yDataInVolt =  yData / 1000

logOfyData = np.log(yDataInVolt)

#Plot experimental data points
plt.plot(xData, logOfyData, 'bo', label='experimental-data')

# Initial guess for the parameters
initialGuess = [500,485]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData, logOfyData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0.500, 4.5000, 0.001)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params f(x)=a*x +b and \u03C4_C:=-1/a: a=%5.3f, b=%5.3f' % tuple(popt))
plt.title('TV5 Plot1:Beziehung zw. log(Spannung) und Zeit')
plt.xlabel('Zeit(t) /s')
plt.ylabel('log(Spannung(y)) /V')
plt.legend()
plt.show()
import math

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

PI = math.pi
#Fitting function
def func(x, a,b):
    return (a/(4*np.pi*((x)**2))+b)
    #return a*x+b

#Experimental x and y data points
xData = np.array([1.6,2.6,3.6,4.6,5.6,6.6,7.6,8.6,9.6,10.6,11.6,12.6,13.6,14.6,15.6,16.6]) # NET Distance from lamp in cm
xError = 0.1 #Error from ruler, symettric +/- 0.1 in cm
yData = np.array([70000,30300,16500,11100,8100,5500,4600,3000,2900,2500,2000,1700,1400,1200,1000,900])#Measured Vales (Beleuchtungsstaerke) from Luxmeter in lux

yErrorAr = [5000,500,100,200,100,200,100,100,50,50,50,50,50,50,50,50]            #Error from the luxmeter in lux +/- symettric

#Plot experimental data points
plt.plot(xData, yData, 'bo', label='experimental-data')
plt.errorbar(xData,yData,xerr=xError, yerr=yErrorAr ,ecolor='green', fmt = 'none' ,label='errorBar')
# Initial guess for the parameters
initialGuess = [2209722,0]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData, yData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(1, 20, 0.01)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='f(x):=(a/(4*np.pi*((x)**2))+b) :a=%5.3f  b=%5.3f' % tuple(popt))
plt.title('TV3:Photometrical Distance Law Experiment')
plt.xlabel('x-Axis:Net Distance between luxmeter and lamp in cm')
plt.ylabel('y-Axis:The measured value from luxmeter in lx')
plt.legend()
plt.show()

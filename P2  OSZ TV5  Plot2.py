import math

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

var=0



#Fitting function
def func(x, a, b):
    return a*x+b

    #return a*x+b
print('var=',var)
#Experimental x and y data points
xData = np.array([0.200, 0.400, 0.600,0.800,1.000,1.200,1.400,1.600,1.800]) #t in s
yData = np.array([5.62,3.73,2.45,1.61,1.02,0.643,0.395,0.238,0.135])  #y in V

xDataUncertainty =xData / 10

xDataPlusUncertainty =xData+ xDataUncertainty
xDataMinusUncertainty = xData- xDataUncertainty


logOfyData =np.log(yData)

#Plot experimental data points
plt.plot(xData, logOfyData, 'bo', label='experimental-data +/- delta')
plt.plot(xDataPlusUncertainty, logOfyData, 'bo',)
plt.plot(xDataMinusUncertainty, logOfyData, 'bo',)


# Initial guess for the parameters
initialGuess = [500,485]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData, logOfyData, initialGuess)
popt2, pcov2 = curve_fit(func, xDataPlusUncertainty, logOfyData, initialGuess)
popt3, pcov3 = curve_fit(func, xDataMinusUncertainty, logOfyData, initialGuess)
print(popt)
print(popt2)
print(popt3)

#x values for the fitted function
xFit = np.arange(0.200, 1.800, 0.001)
xFit2 = np.arange(0.22, 1.980, 0.001)
xFit3 = np.arange(0.18,1.720,0.001)
print('var=',var)
#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params:f(x)=a*x+b and \u03C4_C:=-1/a,a=%5.3f, b=%5.3f'% tuple(popt))
plt.plot(xFit2, func(xFit2, *popt2), 'r', label='fit params:f(x)=a*x+b and \u03C4_C:=-1/a,a=%5.3f, b=%5.3f'% tuple(popt2))
plt.plot(xFit3, func(xFit3, *popt3), 'r', label='fit params:f(x)=a*x+b and \u03C4_C:=-1/a,a=%5.3f, b=%5.3f'% tuple(popt3))

plt.title('TV5 Plot 2:Beziehung zw. Spannung und Zeit')
plt.xlabel('Zeit(t) /s')
plt.ylabel('Spannung(y) /V')
plt.legend()
plt.show()
print('var=',var)
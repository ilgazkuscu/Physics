import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*(x**(1/2)) + b
    #return a*x+b

#Experimental x and y data points
xData = np.array([118,75,90,53])#Abstand to square
yData = np.array([71.61,56.3,64.9,31.72 ]) #Period in sec


#plot is x-y^2 ; y= ax + b ; a in [cm / s^2]
xError = 0.0036 # in mm
yError = 0.2

xData2 = (xData/100)*(xData/100)


#Plot experimental data points
plt.plot(xData2, yData, 'bo', label='experimental-data')
plt.errorbar(xData2,yData, xerr=xError, yerr=yError, label ='errorBar', fmt ='none')

# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData2, yData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0.0, 3, 0.01)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x^2 Abstand / m')
plt.ylabel('y period / s')
plt.legend()
plt.show()
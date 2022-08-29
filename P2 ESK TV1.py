import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#CHECK THE FORMAT & LEGEND it is not right! LLA TV2ALU-like should it seem!!
def func(x, a, b):
    return a*x + b
    #return a*x+b


#Experimental x and y data points
xData = np.array([11.36,12.32,13.44,14.64,15.5, 16.27,17.40,18.30,19.5,20.79,21.7,23.8]) #Strom in mA
yData = np.array([1.334,1.333,1.329,1.327,1.324,1.322,1.319,1.319,1.314,1.314,1.310,1.306]) #Spannung in V

plt.plot(xData, yData, 'bo', label='experimental-data')
initialGuess = [1,1]
popt,pcov = curve_fit(func, xData, yData)


#x values for the fitted function
xFit = np.arange(0, 1.0, 0.025)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params f(x)=ax+b: a=%5.3f, b=%5.3f' % tuple(popt))
plt.title("TV1")
plt.xlabel('(cos(\u03A6) / cos(\u03A6 = 15\u00B0 )')
plt.ylabel('U(cos(\u03A6) / U(cos\u03A6 = 15\u00B0 ))')
plt.show()
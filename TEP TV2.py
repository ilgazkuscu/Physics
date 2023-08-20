import math

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
 return a*x+b
 #return a*x+b

#Experimental x and y data points
xData = np.array([89.9, 74.8, 59.8, 44.8, 29.8, 14.8]) # T in degree Celsius
yData = np.array([723.2, 699.2, 674.2, 651.2, 628.2, 593.2])#Druck in mmHg
Quotient = yData / 654.2
kolbenVolumen = yData * yData * math.pi #Kolbe ist ein Zylinder V_zyl = pi * r*r*h

xError = 0.1 #ReadingError
yError = 0.2 #ReadingError + ApparatusError


#Plot experimental data points
plt.plot(xData, Quotient, 'bo', label='experimental-data')

# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData,   Quotient, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0.0, 90.0, 0.1)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.4f, b=%5.4f' % tuple(popt))

plt.xlabel('T / grad Celsius')
plt.ylabel('Volumenproportion:(V/V_0) [o.Einheit]')
plt.title('TV4:Bestätigung des Gesetzes von Gay-Lussac')
plt.legend()
plt.show()
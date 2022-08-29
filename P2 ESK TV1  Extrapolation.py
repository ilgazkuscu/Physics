import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x+b
    #return a*x+b

##Experimental x and y data points
xData = np.array([11.36,12.36,13.36,14.36,15.36, 16.36,17.36,18.36,19.36,20.36,21.36,22.36]) #Strom in mA
yData = np.array([1.334,1.333,1.329,1.327,1.324,1.322,1.319,1.319,1.314,1.314,1.310,1.306]) #Spannung in V

xDataInAmpere = xData / 1000 #mA > A:durch 1000 dividieren


 #ARGUMENT:Die Messungen sind nicht aquidistant wie gewünscht deswegen geht plot nach unten um die Pkte verbinden zu können.




#Plot experimental data points
plt.plot(xDataInAmpere, yData, 'bo', label='experimental-data')

# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit
popt, pcov = curve_fit(func, xDataInAmpere, yData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0.0, 0.022236, 0.00001)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='f(x)=ax+b: a=%5.5f, b=%5.5f \u03A9= abs(a)' % tuple(popt))

plt.xlabel('Strom / A')
plt.ylabel('Spannung / V')
plt.title("TV1 (IDEAL MEASUREMENT) Extrapolation auf (I=0)")
plt.legend()
plt.show()
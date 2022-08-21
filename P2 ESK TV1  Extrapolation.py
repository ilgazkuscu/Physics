import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x+b
    #return a*x+b

##Experimental x and y data points
xData = np.array([11.36,12.32,13.44,14.64,15.5, 16.27,17.40,18.30,19.5,20.79,21.7,23.8]) #Strom in mA
yData = np.array([1.334,1.333,1.329,1.327,1.324,1.322,1.319,1.319,1.314,1.314,1.310,1.306]) #Spannung in V


 #ARGUMENT:Die Messungen sind nicht aquidistant wie gewünscht deswegen geht plot nach unten um die Pkte verbinden zu können.




#Plot experimental data points
plt.plot(xData, yData, 'bo', label='experimental-data')

# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData, yData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0.000, 34.0000, 0.00001)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params f(x)=ax+b: a=%5.5f, b=%5.5f' % tuple(popt))

plt.xlabel('Strom / mA')
plt.ylabel('Spannung / V')
plt.title("TV1 Extrapolation auf (I=0)")
plt.legend()
plt.show()
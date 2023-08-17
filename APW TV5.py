import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x + b
    #return a*x+b

#Experimental x and y data points
xData = np.array([100,120,140,160,180,200,210,220,230,240,250])#Temperature to be converted to -1/T in Celsius**
yData = np.array([1,2,4,6.5,11,15.5,20,23.5,29,34.5,41]) #Pressure in Bar to be ln(p)

yDataError = 0.1

xDataInKelvin = xData + 273.15 # xData in Kelvin

OneOverMinusxDataInKelvin = -1 / xDataInKelvin
logOfyData = np.log(yData)


lnOfyData = np.log(yData)
#Plot experimental data points
plt.plot(OneOverMinusxDataInKelvin, lnOfyData, 'bo', label='experimental-data')

# Initial guess for the parameters
initialGuess = [4000,12]
#Perform the curve-fit
popt, pcov = curve_fit(func, OneOverMinusxDataInKelvin, lnOfyData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(-0.0027,-0.0019,0.0001)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params f(x)=ax+b a=%5.15f, b=%5.15f' % tuple(popt))
plt.title('TV4 Bezug zw. -1/T und Druck')
plt.xlabel('-1/T / K')
plt.ylabel('Druck /bar')
plt.legend()
plt.show()
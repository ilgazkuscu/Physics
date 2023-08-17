import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x + b
    #return a*x+b

#Experimental x and y data points
xData = np.array([44,62.6,81.5,97,108,119.5,129.6,139.5,148.3,157.1,164.6,170.2,175.9,181.8,187,199.4,214.3,228.3,240.6,253.1])#Temperature to be converted to -1/T in Celsius**
yData = np.array([0.5,0.8,0.8,1,1,1.5,2,3,4,5,6,7,8.5,10,11,16,22,29,36,45]) #Pressure in Bar to be ln(p)

yDataError = 0.1

xDataInKelvin = xData + 273.15 # xData in Kelvin

OneOverMinusxDataInKelvin = -1 / xDataInKelvin
logOfyData = np.log(yData)

xError = ((((OneOverMinusxDataInKelvin**2) * 0.1 ))**(2)) ** (1/2)
yError = ((((1/yData) * 0.1 ))**(2)) ** (1/2)
lnOfyData = np.log(yData)
#Plot experimental data points
plt.plot(OneOverMinusxDataInKelvin, lnOfyData, 'bo', label='experimental-data')
plt.errorbar(OneOverMinusxDataInKelvin, lnOfyData , xerr = xError, yerr=yError, fmt = 'none' ,label='errorBar due to Reading')
print("yErrorRelative:",abs (yError /lnOfyData))
# Initial guess for the parameters
initialGuess = [4000,12]
#Perform the curve-fit
popt, pcov = curve_fit(func, OneOverMinusxDataInKelvin, lnOfyData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(-0.0027,-0.0019,0.0001)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params f(x)=ax+b a=%5.15f, b=%5.15f' % tuple(popt))
plt.title('TV4 Bezug zw. -1/T und ln(Druck)')
plt.xlabel('-1/T / K^(-1)')
plt.ylabel('ln(p) /bar')
plt.legend()
plt.show()
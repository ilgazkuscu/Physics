import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x + b
    #return a*x+b

#Experimental x and y data points
xData = np.array([11.37,11.27,10.68, 9.86, 9.72,9.17,8.77,8.42,8.14,7.79,7.61,7.08,6.93,6.68,6.42,6.22,6.08,5.74])#t in s +/- needed , t^2 needed;
yData = np.array([85,78.5,73,66,62,58,54,51,48,45.5,43.5,41,39,36.5,35,33,32.5,31]) #h / in cm


#plot is x-y^2 ; y= ax + b ; a in [cm / s^2]
xError = 0.4 # 0.2 sec of reaction time

yError = 1 #0.1m augenmass misinterpretation

xData2 = xData*xData


#Plot experimental data points
plt.plot(xData2, yData, 'bo', label='experimental-data')
plt.errorbar(xData2,yData, xerr=xError, yerr=yError, label ='errorBar', fmt ='none')

# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData2, yData, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0.0, 144, 0.01)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x in s^2 T^2')
plt.ylabel('y height in cm')
plt.legend()
plt.show()
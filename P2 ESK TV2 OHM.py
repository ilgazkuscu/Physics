import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit
import numpy as np



#Fitting function
def func(x, a, b):
    return a*x+b
    #return a*x+b

#Experimental x and y data points Erwartung:lineares Verfahren zw. U und I deren Tangens die R ergibt.
xData = np.array([0,2.01,4.01,6.02,8.01,10.01,11.99,14.09,16.01,18.06,19.77])#gemessene Spannung in V
yData = np.array([0,0.00061,0.00122,0.00183,0.00245,0.00308,0.00367,0.00429,0.00491,0.00553,0.00608 ]) #gemessener Strom in mA

xDataError = (xData * 9 / 100) + (4*10**(-4))#uncertainty of percent & the last digit uncertainty
yDataError = (yData * 1 / 100) + (5*10**(-4))

print(yDataError)
plt.errorbar(xData, yData, xerr =xDataError, yerr = yDataError,
             fmt='none')
plt.errorbar(xData,yData,yerr=yDataError,)
plt.plot(xData,yData)
#Plot experimental data points

# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit


#x values for the fitted function
popt, pcov = curve_fit(func, xData, yData, initialGuess)
print(popt)
xFit = np.arange(0.0, 0.0100, 0.01)
plt.plot(xData, yData, 'bo', label='experimental-data')


plt.title("Klassische Kennlinie eines Ohm'schen Stromkreises")
plt.plot(xFit, func(xFit, *popt), 'b', label='fit params f(x)=a*x+b: a=%5.8f, b=%5.8f' % tuple(popt))

plt.xlabel('Spannung / V')
plt.ylabel('Strom / A')
plt.legend()
plt.show()

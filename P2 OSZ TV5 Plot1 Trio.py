import math

import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x +b
    #return a*x+b

#Experimental x and y data points
xData = np.array([0.500, 1.000, 1.500,2.000,2.500,3.000,3.500,4.000,4.500]) #t in ms
yData = np.array([485,273,163,89.8,50.8,33.8,12.8,11.3,4.5]) #U_C :y in mV  :Kondensatörün haznesindeki gerilim miktarı; zaman içinde boşalıyor.

U_0 = 485 #in mV
U_CDividedByU_0 = yData /U_0 # U_C / U_0  =:y
yDataEmptied = U_0 - yData # Emptied amound FROM the Condensator. U_0 - U_C

lnOfU_CDividedByU_0 =np.log(yData / U_0)

logOfU_CDividedByU_0 =numpy.gradient(lnOfU_CDividedByU_0)

logOfU_CDividedByU_0DividedByU_CDividedByU_0 =numpy.gradient(lnOfU_CDividedByU_0) / U_CDividedByU_0

absoluteValueOfDeltaOverY = abs(logOfU_CDividedByU_0DividedByU_CDividedByU_0) # takes absolute value Of log(U_c / U_0) / y

absoluteValueOfDeltaOverYInVolt  = absoluteValueOfDeltaOverY / 1000

yDataUncertainty = absoluteValueOfDeltaOverYInVolt #uncertainty in Volt

print('lnOfU_CDividedByU_0' , lnOfU_CDividedByU_0,'numpy.gradient(lnOfU_CDividedByU_0) = delta m(Steigung)',absoluteValueOfDeltaOverYInVolt)

xDataUncertainty = xData / 10 # Tau_Hersteller ergibt sich 10%  nach der Gauss
yDataInVolt =  yData / 1000 #y in mV -> y in V

logOfyData = np.log(yDataInVolt) #log of y in V

xDataPLUSxDataUncertainty = xData + xDataUncertainty
xDataMINUSxDataUncertainty = xData - xDataUncertainty

yDataPLUSyDataUncertainty = logOfyData + yDataUncertainty
yDataMINUSxDataUncertainty = logOfyData - yDataUncertainty

print('xerr=xDataUncertainty,',  xDataUncertainty, 'yerr=yDataUncertainty' , yDataUncertainty)
print('xDataPLUSxDataUncertainty',xDataPLUSxDataUncertainty)
#Plot experimental data points

plt.plot(xData, logOfyData, 'bo', label='experimental-data +/- Delta')
plt.plot(xDataPLUSxDataUncertainty, logOfyData, 'bo', )
plt.plot(xDataMINUSxDataUncertainty, logOfyData, 'bo',)
plt.errorbar(xData,logOfyData,xerr=xDataUncertainty,yerr=yDataUncertainty)
# Initial guess for the parameters
initialGuess = [500,485]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData, logOfyData, initialGuess)
popt2,pcov = curve_fit(func,xDataPLUSxDataUncertainty,logOfyData,initialGuess)
popt3,pcov = curve_fit(func,xDataMINUSxDataUncertainty,logOfyData,initialGuess)

print(popt)

#x values for the fitted function
xFit = np.arange(0.500, 4.5000, 0.001)
xFit2 = np.arange(0.550, 4.9500, 0.001)
xFit3 = np.arange(0.450, 4.0500, 0.001)

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='f(x)=a*x+b,\u03C4_C=-1/a: a=%5.3f, b=%5.2f' % tuple(popt))
plt.plot(xFit2, func(xFit2, *popt2), 'r', label='f(x)=a*x+b,\u03C4_C=-1/a: a=%5.3f, b=%5.2f' % tuple(popt2))
plt.plot(xFit3, func(xFit3, *popt3), 'r', label='f(x)=a*x+b,\u03C4_C=-1/a: a=%5.3f, b=%5.2f' % tuple(popt3))

plt.title('TV5 Plot1:Beziehung zw. log(Spannung) und Zeit')
plt.xlabel('Zeit(t) /s')
plt.ylabel('log(Spannung(y)) /V')
plt.legend()
plt.show()
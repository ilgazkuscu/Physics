import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x + b
    #return a*x+b

#Experimental x and y data points
xData = np.array([8.74,8.33,8.12,7.64,7.52,7.15,6.79,6.67,6.32,6.21,5.82,6.43,6.44,3.43,5.04,4.88,4.75,4.34,4.31,4.13,3.57])#t in s +/- needed , t^2 needed;
yData = np.array([66,63,59.5,57,54.5,51.5,49.5,47.5,45,43.5,42,40.5,39,37,36.5,35.5,35,33.7,33,33.5,32.5]) #h / in cm



#plot is x-y^2 ; y= ax + b ; a in [cm / s^2]
xError = 0.4 # 0.2 sec of reaction time

yError = 1 #0.1m augenmass misinterpretation
#Zur Erzugung der Fehlgeraden, x_opt + DeltaX, x_opt_ - DeltaX und deren Funktionswerte als zusatzliche Geraden zu plotten.
xDataPlusUncertainty = xData + xError
xDataMinusUncertainty = xData - xError
yDataPlusUncertainty = yData + yError
yDataMinusUncertainty = yData - yError


xData2 = xData * xData
xData3 = xDataPlusUncertainty * xDataPlusUncertainty
xData4 = xDataMinusUncertainty * xDataMinusUncertainty


#Plot experimental data points
plt.plot(xData2, yData, 'bo', label='experimental-data')
plt.plot(xData3, yDataPlusUncertainty, 'bo', label='experimental-data')
plt.plot(xData4, yDataMinusUncertainty, 'bo', label='experimental-data')

plt.errorbar(xData2,yData, xerr=xError, yerr=yError, label ='errorBar', fmt ='none')

# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit
popt, pcov = curve_fit(func, xData2, yData, initialGuess)
popt2, pcov = curve_fit(func, xData3, yDataPlusUncertainty, initialGuess)
popt3, pcov = curve_fit(func, xData4, yDataMinusUncertainty, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(8, 82, 0.01)
xFit2 = np.arange(8, 82, 0.01)
xFit3 = np.arange(8, 82, 0.01)



#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))
plt.plot(xFit2, func(xFit2, *popt2), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt2))
plt.plot(xFit3, func(xFit3, *popt3), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt3))

plt.title('Maxwell Wheel T^2 and Height Relation with with Error Bars')
plt.xlabel('x in s^2 T^2')
plt.ylabel('y height in cm')
plt.legend()
plt.show()
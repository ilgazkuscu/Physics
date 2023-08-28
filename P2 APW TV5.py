import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return a*x + b
    #return a*x+b

#Experimental x and y data points
xData = np.array([80,100,130,160,190,210,240,270,300,330,350])#Temperature measured in Celsius to be converted to Kelvin
yData = np.array([0.019,0.021,0.033,0.049   ,0.069,0.079,0.110,0.138,0.172,0.222,0.255]) #Voltage measured in mV to be converted to V

yDataError = 0.002 # Ablesefehler vom Spannungsgerat
yDataErrorInVolt =yDataError / 1000
xError = 0.2#Ablesefehler v. Temperatur in Grad
xDataError =(4*xData**(3) * xError)**(1/2)#xError Propogated in Grad

xDataInKelvin = xData + 273.15 # xData in Kelvin
yDataInVolt = yData / 1000
RoomTemp=26.6+273.15

xDataError=(xDataInKelvin**(4)-RoomTemp**(4))/50 #1% error
yDataError= 0.000001


plt.errorbar(xDataInKelvin**(4)-RoomTemp**(4),yDataInVolt,xerr=xDataError,yerr=yDataErrorInVolt , fmt = 'none' ,label='errorBar')

lnOfyData = np.log(yData)
#Plot experimental data points
plt.plot(xDataInKelvin**(4)-RoomTemp**(4), yDataInVolt, 'bo', label='experimental-data')

# Initial guess for the parameters
initialGuess = [2.5*10**(-15),9.9*10**(-6)]

#Perform the curve-fit
popt, pcov = curve_fit(func, xDataInKelvin**(4)-RoomTemp**(4), yDataInVolt, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(6*10**(9), 1.5*10**(11), 10**(6))

#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params f(x)=ax+b a=%5.15f, b=%5.15f' % tuple(popt))
plt.title('TV5 Bezug zw. T^4-(T_0)^4 , gemessener Spannung')
plt.xlabel('T^4-(T_0)^4 / K')
plt.ylabel('gemessene Spannung /V')
plt.legend()
plt.show()
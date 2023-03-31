import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return x* a + b
    #return a*x+b

#Experimental x and y data points
xData = np.array([0.1 , 52 , 101 ,152 , 201 , 248  , 298 , 349 , 398 , 448]) #filled water in gram almost equal to volume of the bottle
yData = np.array([165.53 , 172.85 , 186.04 , 200.68,  216.80 , 243.16 , 262.21 , 303.22  ,370.61 , 511.23  ]) #f:frequency in Hz
V_0AirVolume = 500 - xData #Ann:Dichte_Wasser = 1 deswegen direkt abgezogen
OneDividedByV_0AirVolume = 1 / V_0AirVolume
yData2 = yData*yData
print(yData2)

xError =0.0005 #0.5g Küchenwaage Unsicherheit

#Plot experimental data points
plt.plot(OneDividedByV_0AirVolume, yData2, 'bo', label='experimental-data')
plt.errorbar(OneDividedByV_0AirVolume, yData2 , xerr= xError, fmt = 'none' ,label='errorBar due to kitchen scale')
# Initial guess for the parameters
initialGuess = [1.0,1.0]

#Perform the curve-fit
popt, pcov = curve_fit(func, OneDividedByV_0AirVolume, yData2, initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0.0, 0.03, 0.0001)



#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))
plt.title('Helmholtz Resonator Bottle 2 (Frequency^2) and (1/Air Volume) Relation')
plt.xlabel('1/V_0 /ml')
plt.ylabel('f^2 / Hz^2')
plt.legend()
plt.show()
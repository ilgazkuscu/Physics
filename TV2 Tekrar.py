import math

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#Fitting function
def func(x, a, b):
    return x* a + b
    #return a*x+b

#Experimental x and y data points

betaDiff =np.array([0,-8,-7,-10,-12,-9,-9,-10,-12,-13])
betaNet = np.array([-8,-15,-25,-37,-48,-57,-67,-79,-92])
betaAngle = np.array([75,67,60,50,38,27,18,8,-4,-13]) #beta angle from torsion in degree upper
alphaAngle = np.array([0,10, 20, 30, 40, 50, 60, 70, 80, 90]) #alpha angle from torsion in degree
xError =7 #Error of Phi due to 4 degrees of error of both alpha and beta (via Gaussian)
Beta_0 = 75 #0-Setting for the beta angle, const. in degree
Delta_Alpha_0 = 4# the alpha angle unc.
betaAngleNet = betaAngle - Beta_0
phi = alphaAngle - betaDiff

Phi = alphaAngle - betaAngleNet #beta angle from torsion in degree upper #Phi:=Torsion angle
yDataSin =np.sin(np.deg2rad(alphaAngle))#sin(alpha) from torsion cable


print(Phi)
print(yDataSin)
print(betaAngleNet)
print(phi)
#Plot experimental data points
plt.plot(phi, (yDataSin), 'bo', label='experimental-data')
plt.errorbar(phi, (yDataSin) , xerr= xError, fmt = 'none' ,label='errorBar v.Winkel')
# Initial guess for the parameters
initialGuess = [1.0,0]

#Perform the curve-fit
popt, pcov = curve_fit(func, phi, abs(yDataSin), initialGuess)
print(popt)

#x values for the fitted function
xFit = np.arange(0, 105,0.1)



#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params:f(x)=ax+b a=%5.3f, b=%5.3f' % tuple(popt))
plt.title('TV2 Beziehung zw. Torsionswinkel Phi und sin(alpha)')
plt.xlabel('Phi / grad')
plt.ylabel('sin(alpha)')
plt.legend()
plt.show()
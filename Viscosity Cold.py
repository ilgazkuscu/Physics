import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit
import numpy as np
import statistics
diameterArray = np.array([0.3,0.3,0.6,1.3,1.0,0.4,0.5,0.3,0.5,0.5]) # in cm 2*r_i for each instant -> to divide by 100 s.t in m
distanceArray = np.array([11.6,4.6,4.6,5.6,17.6,15.6,16.6,13.6,12.6,15.6]) # in cm -> to divide by 100 s.t in m
timeArray = np.array([47.3,37.07,5.6,1.27,5.32,15.9,15.4,58.77,21.25,39.07])# in s
noOfExperiments = 10

velocityArray = distanceArray / timeArray # in cm / s

velocityArrayInMeterPerSecond = velocityArray / 100
diameterArrayInMeter = diameterArray / 100

rhoConstant = 1000 #in kg / m^^
gravityConstant = 9.81 # in m / s^^
constantOfEq = gravityConstant * 2 *rhoConstant / 9 #m/s^2 * kg / m^3 = kg / (m^2 s^2)
radiusArray = diameterArrayInMeter / 2 #in meter
radiusArraySquared = radiusArray * radiusArray #in meter^2

mu_SpülmittelArray =radiusArraySquared * constantOfEq / velocityArrayInMeterPerSecond #( kg/(m^2 s^2)) * m^2 /(m/s) = kg / s^2

mu_SpülmittelArrayMeanAvg =statistics.mean(mu_SpülmittelArray)

print("diameterArrayInMeter" , diameterArrayInMeter)
print("velocityArrayInMeterPerSecond" , np.round_(velocityArrayInMeterPerSecond , decimals= 5))
print("MU in Pas", np.round_(mu_SpülmittelArray , decimals = 2))

print("mean Viscosity ", mu_SpülmittelArray.mean())
print("Standart Deviation of Viscosity at Cold Temperature is" , statistics.stdev(mu_SpülmittelArray))
print("Relative uncertainty of Viscosity at Cold Temperature Standart Deviation  is " , statistics.stdev(mu_SpülmittelArray) / noOfExperiments**(1/2))

reynoldArray =  velocityArray * radiusArray*2 * 1000 / mu_SpülmittelArray
print("Reynold numbers of our array is ", np.round_(reynoldArray , decimals = 2))
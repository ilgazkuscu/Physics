import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit
import numpy as np
import statistics

timeData =np.array([1.2,1.01,1.07,0.8,1.13]) #in s
distanceTraveledData = np.array([15.5, 15.5, 15.5,15.5, 15.5]) # in cm
distanceTraveledDataInMeters = distanceTraveledData / 100
velocityData = distanceTraveledDataInMeters / timeData #in m / s



print(np.round(velocityData, decimals=5))
print("mean velocity is," , statistics.mean(velocityData))




import sys
import os
import arcpy
import numpy as np
import matplotlib.pyplot as plt 


"""
python code to plot some general accuracy statistics 
"""
#Input raster
inRas = arcpy.Raster(r"D:...")

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(inRas, nodata_to_value=-100)

#Counter
arr = arr[arr != -100] #remove all no values
one_d = arr.flatten()
array_int = np.array(one_d, dtype='int')
recurrence = np.bincount(array_int, minlength=360) #360 in case of aspect, 91 slope

#Compute the percentage
tot = len(one_d)
float_rec = np.array(recurrence, dtype='float')
percentage = np.divide(float_rec, tot)*100

# print(percentage)
# print(recurrence)

#generate x_axis
x= np.arange(360) #uncomment in case of aspect
#x = np.arange(91)


#plot the result (Aspect)

# line plot
plt.figure(figsize=(8,5))
plt.plot(x, percentage)

plt.xticks(np.arange(0, 405, 45))
plt.xlim(0,361)
plt.ylim(0,0.6)
plt.xlabel('Aspect [Degrees]', fontsize=18)
plt.ylabel('Percentage [%]', fontsize=18)
plt.title('Aspect values distribution', weight='bold', fontsize=14)
plt.tight_layout()
plt.tick_params(labelsize=16)
#plt.savefig(r"D:\...") # uncomment to save the plot 
plt.show()  # shows the plot 

"""
# Other Plot: Histogram (Slope)
plt.figure(figsize=(8,5))
plt.bar(x, percentage) #edgecolor = "black"
plt.xticks(np.arange(0, 90, 15))
#plt.xlim(0,90)
plt.xlabel('Slope [Degrees]', fontsize=18)
plt.ylabel('Percentage [%]', fontsize=18)
plt.title('Slope Values Distribution', weight='bold', fontsize=14)
plt.xlim(0, 75)
plt.tick_params(labelsize=16)
plt.tight_layout()
#plt.savefig(r"D:\...") # uncomment to save the plot 
plt.show()  # shows the plot
"""
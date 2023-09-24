import matplotlib.pyplot as plt
import matplotlib
import pandas as pd 
import numpy as np
from scipy.signal import find_peaks
def align_minema(data_1,data_2):
    len1 = len(data_1)
    len2 = len(data_2)
    min_1 = np.argmin(data_1[int(len1/2 - len1/4):int(len1/2 + len1/4) ])
    min_2 = np.argmin(data_2[int(len2/2 - len2/4):int(len2/2 + len2/4)])
    print(min_1,min_2)
    diff = np.abs((min_1+int(len1/2 - len1/4))-(min_2+int(len2/2 - len2/4)))
    if (min_1+int(len1/2 - len1/4)) > (min_2+int(len2/2 - len2/4)):
        data_1_r = data_1[diff:]
        data_2_r = data_2
    else:
        data_1_r = data_1
        data_2_r = data_2[diff:]
    pixel = np.arange(0,len(data_1_r))
    print(len(data_1_r),len(data_2_r),len(data_1),len(data_2))
    return data_1_r,data_2_r,pixel

data_h = pd.read_csv("C:\\Bac_Arbeit\\ratumi_bac\\bac_template\\code\\data\\horizontalline_2hpc_700mV.csv", delimiter= ",")
data_v = pd.read_csv("C:\\Bac_Arbeit\\ratumi_bac\\bac_template\\code\\data\\verticalline_2hpc_700mV.csv", delimiter= ",")
data_h_m = pd.read_csv("C:\\Bac_Arbeit\\ratumi_bac\\bac_template\\code\\data\\horisontalline_2hpc_mgo_250mv.csv", delimiter= ",")
data_v_m = pd.read_csv("C:\\Bac_Arbeit\\ratumi_bac\\bac_template\\code\\data\\verticalline_2hpc_mgo_250mv.csv", delimiter= ",")


I_1, I_2, pixel = align_minema(data_h_m["Gray_Value"],data_v_m["Gray_Value"])
pixel1 = (np.arange(0,len(I_1))/98)*13
pixel2 = (np.arange(0,len(I_2))/98)*13
#plt.plot(pixel,I_1,I_2)
plt.style.use('bmh')
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 16}

matplotlib.rc('font', **font)
plt.plot(pixel1,I_1,"r")
plt.plot(pixel2,I_2,"b")
plt.xlabel("$\AA $")

plt.show()
plt.cla()
plt.plot(data_h["Distance_(pixels)"],data_h["Gray_Value"])
plt.plot(data_v["Distance_(pixels)"],data_v["Gray_Value"])
#plt.show()
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as  mlab
import math
import scipy.stats as sp

def Q1() :
    
    x = [2159,2192,2204,2628,2643,2687,3049,3273,3394,3432,3642]
    y = [65.7,38.3,63.8,69.6,26.2,24.7,4.9,5.7,14.8,4.0,3.0]
    plt.plot(x,y)
 
def Q2() :
    
    x = [3642,3432,3049,3273,3394,2687,2643,2192,2204,2159,2628]
    y = [3.0,4.0,4.9,5.7,14.8,24.7,26.2,38.3,63.8,65.7,69.6]
    moyx = np.mean(x)
    moyy = np.mean(y)
    temp1 = 0
    temp2 = 0

    for i in range(len(x)) :
        temp1 += x[i] - moyx
    
    for i in range(len(y)) :
        temp2 += y[i] - moyy

    
    B1 = (temp1 * temp2) / (temp1 ** 2)
    B0 = moyy - (moyx * B1)
    print ("B1 :",B1,"\n")
    print ("B0 :",B0,"\n")
    return


Q1()
Q2()
plt.show()

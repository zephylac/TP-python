import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as integrate


def Q1(nb_val) :
        a = []
        j = 0.0
        for i in range(1,nb_val+1) :
                x = random.random()
                y = random.random()
                
                
                res = np.sqrt((1 - x*x))
                if res > y : 
                        j += 1
                        a.append((4*j)/i)
        pr = (4*j) / nb_val
        print ("Pourcentage :",pr,"\n")
        
        
        x = np.linspace(0,len(a),len(a))
        plt.plot(x,a)
        plt.show()

Q1(10000)


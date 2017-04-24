import matplotlib.pyplot as plt
import random

def Q1() :
        a = []
        for i in range(0,100000) :
                sum = 0
                for j in range(0,3) :
                        sum += random.randint(1,6)
                a.append(sum)
        print (a)
        print(len(a))
        plt.hist(a, bins='auto')



Q1()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as  mlab
import math
import scipy.stats as sp

def creer_perso(nb_valeur) :
    
    #POIDS#

    y = np.linspace(0,100,nb_valeur)
    
    variance = 30
    mu = 70
    sigma = math.sqrt(variance)
    #plt.plot(y,sp.norm.pdf(y,mu,sigma))

    
    #TAILLE#
    y2 = np.linspace(100,300,nb_valeur)
    
    variance2 = 30
    mu2 = 160
    sigma2 = math.sqrt(variance2)
    #plt.plot(y2,sp.norm.pdf(y2,mu2,sigma2))

    t = sp.norm.pdf(mu2, sigma2, nb_valeur)
    p = sp.norm.pdf(mu, sigma, nb_valeur)
    dic = {"taille":t, "poids":p}
    
    return dic


def Q2(nb_valeur) :
    
    y = np.linspace(-2,2,100)
    
    variance = 0.2
    mu = 0
    sigma = math.sqrt(variance)
    plt.plot(y,sp.norm.pdf(y,mu,sigma))
    return

def Q3(nb_valeur) :
    
    y = np.linspace(-2,2,nb_valeur)
    
    variance = 0.2
    mu = 20
    sigma = math.sqrt(variance)
    plt.plot(y,sp.binom.pmf(y,mu,sigma))
    return

def Q4() :
    fichier = open("stat.txt","r")
    valeurs = fichier.readlines()
    
    valeurs = list(map(float,valeurs))

    fichier.close
    print(valeurs)

    moy = (sum(valeurs))/(len(valeurs))
    print("moyenne :", moy)
    return

def Q4b() :
    fichier = open("stat.txt","r")
    valeurs = fichier.readlines()
    valeurs = list(map(float,valeurs))
    fichier.close
    plt.hist(valeurs, bins='auto')
    return




Q4b()
plt.show()
#test = creer_perso(100)
#print(test)

#Q2(1000)
#Q3(1000)
#plt.show()



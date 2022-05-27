
from fileinput import filename
from math import *
import numpy as np
import matplotlib.pyplot as plt


xmin = -2
xmax =  3
step = 0.001
plt.figure(figsize=(10,15))
plt.ylim([-5,5])
plt.xlim([xmin,xmax])

def integr_family(func,mx=0,my_range = np.linspace(-5,5,10)):
    for my in my_range:
        X = [mx]
        i = mx - step
        while min(X) > xmin:
            X.append(i)
            i-=step
        i = mx + step
        while max(X) < xmax:
            X.append(i)
            i+=step
        X = np.array(X)
        X.sort()
        index_of_mx= np.where(X == mx)[0][0]

        Y_right = []
        Y_left = []
        dx = step
        #Расчитываем положительный ход
        y = my
        for x in X[index_of_mx:-1]:
            kn = func(x,y)
            dy = kn*dx
            yn = y + dy
            Y_right.append(yn)
            y = yn
        #Расчитываем отрицательный ход
        y = my
        for x in X[index_of_mx:0:-1]:
            kn = func(x,y)
            dy = kn*dx
            yn = y - dy
            Y_left.append(yn)
            y = yn

        Y_left.reverse()
        #Склеиваем
        Y = Y_left+[my]+Y_right
        plt.plot(X,Y,'-b',mx,my,'ro')
    plt.grid()
    plt.show()
    
    
    


integr_family(lambda x,y : (y**2-x**2)/(2*x*y) ,mx=2,my_range=np.linspace(1,5,10))
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
x=np.linspace(0,5,50)
def func(x,a,b,c):
    y=a*np.exp(-b*x)+c
    return y

y=func(x,1,2,3)
# add noise
yi=y+0.2*np.random.normal(0,1,size=len(y))
#call curve_fit function
popt,pconv=curve_fit(func,x,yi)
a,b,c=popt
plt.plot(x,yi,"bo",label="data")
plt.plot(x,func(x,a,b,c))
plt.plot(x,y,"r--")
plt.show()

from scipy.interpolate import interp1d
import numpy as np 
import matplotlib.pyplot as plt
x=np.linspace(0,5,10)
y=-x**2
y = y+1.5*np.random.normal(size=len(x))
xfine=np.linspace(0,5,1000)
y0=interp1d(x,y,kind="nearest")
y1=interp1d(x,y,kind="linear")
y2=interp1d(x,y,kind="cubic")
plt.figure()
plt.plot(x,y,"o",label="Data")
plt.plot(xfine,y0(xfine),label="nearest")
plt.plot(xfine,y1(xfine),label="linear")
plt.plot(xfine,y2(xfine),label="cubic")
plt.legend()
plt.grid()
plt.show()



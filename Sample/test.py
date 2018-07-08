import numpy as np
import matplotlib.pyplot as plt


import lagrange as plynm

r = range(4)
k = [3,5, 7, 1]

p= [i for i in range(-10, 11)]
l=[]

for i in p:
    l.append(plynm.lagrange_generator(r, k, i))

x = np.array(p)
y = np.array(l)
xhat = np.array(r)
yhat = np.array(k)

plt.plot(x, y, xhat, yhat)
plt.show()

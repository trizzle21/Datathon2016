import numpy as np
import matplotlib.pyplot as plt

#need to figure out what to import



im = plt.imread("blank.png")
implot = plt.imshow(im)
declare fig, ax = plt.sublot

x = [130, 118, 210, 123]
y= [117,140, 74, 544]
n= [291, 263, 258, 471]

dict1 = dict()

for i in range(0,len(x)):
	dict1[x[i]] = n[i]

axes = plt.gca()
axes.set_xlim([0,430])
axes.set_ylim([0,630])

ax.scatter(x,y,picker=8)
#plt.scatter(x,y)

for i in range(0,4):
	plt.text(x[i], y[i], n[i])


def on_pick(event):
   index = event.ind
   xdata = np.take(x,index)
   ydata = np.take(y,index)
   r = dict1[event.xdata]
   os.system("dataprep.py %s" % r)


fig.canvas.callbacks.connect('pick_event', on_pick)



#need to figure out what to import in order to have a nice canvas. pls.

#plt.canvas.callbacks.connect('pick_event', on_pick)





plt.show()
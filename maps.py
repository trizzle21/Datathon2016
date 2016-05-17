import numpy as np
import matplotlib.pyplot as plt


#from scipy.misc import imread


#img = imread("blank.png")

im = plt.imread("blank.png")
implot = plt.imshow(im)


x = [130, 118, 210, 123]
y= [117,140, 74, 544]
n= [291, 263, 258, 471]

dict1 = dict()

for i in range(0,len(x)):
	dict1[x[i]] = n[i]

axes = plt.gca()
axes.set_xlim([0,430])
axes.set_ylim([0,630])


plt.scatter(x,y)

for i in range(0,4):
	plt.text(x[i], y[i], n[i])


def on_pick(event):
   r = dict1[event.x]
   os.system("dataprep.py %s" % r)





#plt.canvas.callbacks.connect('pick_event', on_pick)


# plt.text(x[0], y[0], n[0])
# plt.text(x[1], y[1], n[1])
# plt.text(x[2], y[2], n[3])
# plt.text(x[2], y[2], n[3])




plt.show()
"""
Takes in a series of x,y points and interpolates them.
(x_1,y_1)(x_2,y_2)(x_3,y_3)

P(x) = ((x -x_2)(x-x_3)/(x_1-x_2)(x_1-x_3))*y_1




"""
import numpy as np

def lagrange_generator(xdata , ydata, x):
	""" Takes in (x,y) arrays, and a x value 
		and solves for P(x) 
	"""

	dx = len(xdata)
	dy = len(ydata)
	
	sum = 0
	L = [0]* dy

	def bas(j, xi):
		v = 1
		for i in xrange(dx):
			if i != j:
				v *= (xi - xdata[i])/(xdata[j] - xdata[i])
		return v
	
	for l in xrange(dy):
		L[l] += ydata[l] * bas(l,x) 

	for k in xrange(dy):		
		sum += L[k]
	
	return int(sum)


def  lagrange_generator_deriv(xdata , ydata, x):
	""" Takes in (x,y) arrays, and a x value 
		and solves for P'(x) 
	"""
	pass
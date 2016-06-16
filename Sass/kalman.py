# Takes in a list of x and y coordinates and outputs three lines. observed data, 
#
# x_k is state estimate (lagrange)
# z_k is observed state
#
#
#
#model 
#	 x_k = x_k−1 + w_k
#	 z_k = h(x_k−1) + v_k

#predict
# 	 x̂_k = x̂_k−1
#	 p_k = p_k−1 + q

#update
#	g_k= pk ckck (ck * pk * ck +r)^−1
#	x̂_k = x̂_k + g_k (z_k − h(x^k)) 
#	p_k= (1− g_k * c_k ) * p_k

import lagrange as lg


def kalmanFilter(observed_data, estimate_state):
	r = .045
	xhat = []
	for i in estimate_state:
		xhat.append(i+(r*i))
	s

	


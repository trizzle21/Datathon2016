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

#linear version
# xhat = a * xhat;
# p    = a * p * a;

# // Update
# g    = p  / (p  + r);
# xhat = xhat + g * (z - xhat);
# p    = (1 - g) * p;


import lagrange as lg


def kalman_filter(observed_data):
	#instance vars
	
	data_len = len(observed_data);
	estimate_data_range = [x for x in range(0,data_len)]
	
	#model building time
	estimate_state = []
	for i in observed_data:



	#prediction
	#TODO



	#update
	#TODO




	#Graphical printout
	#needs (observed data, y), (estimate_state, estimate_data_range), (prediction_line, estimate_data_range) graphed over each other.
	#TODO









	


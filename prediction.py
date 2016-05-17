#Predictive Markov models
#Backwards Forwards is really hard exhauasted
import numpy as np
import pylab as pl
import dataprep 


import numpy as np
import pylab as pl
from pykalman import KalmanFilter

import dataprep


sm = dataprep.OBSERVED_DATA[0:2]




# specify parameters
transition_matrix = [[1, 0.1], [0, 1]]
transition_offset = [-0.1, 0.1]
observation_matrix = np.eye(2) + np.matrix([sm[0],sm[1]][sm[3],sm[4]])
observation_offset = [1.0, -1.0]
transition_covariance = np.eye(2) 
observation_covariance = np.eye(2) + 0#needs covar of observation_matrix
initial_state_mean = 0#need mean
initial_state_covariance = 0#need initial covar

# sample from model
kf = KalmanFilter(
    transition_matrix, observation_matrix, transition_covariance,
    observation_covariance, transition_offset, observation_offset,
    initial_state_mean, initial_state_covariance,
    sm
)
states, observations = kf.sample(
    n_timesteps=50,
    initial_state=initial_state_mean
)

# estimate state with filtering and smoothing
filtered_state_estimates = kf.filter(observations)[0]
smoothed_state_estimates = kf.smooth(observations)[0]

# draw estimates
pl.figure()
lines_true = pl.plot(states, color='b')
lines_filt = pl.plot(filtered_state_estimates, color='r')
lines_smooth = pl.plot(smoothed_state_estimates, color='g')
pl.legend((lines_true[0], lines_filt[0], lines_smooth[0]),
          ('true', 'filt', 'smooth'),
          loc='lower right'
)
pl.show()







   
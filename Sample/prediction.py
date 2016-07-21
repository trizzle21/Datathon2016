'''
===========================================
Using the Kalman Filter and Kalman Smoother
===========================================
This simple example shows how one may apply the Kalman Filter and Kalman
Smoother to some randomly generated data.
The Kalman Filter and Kalman Smoother are two algorithms for predicting the
hidden state of Linear-Gaussian system. In this script, all model parameters
are specified beforehand, so there is no need to fit the Kalman Filter's
parameters to the measurements. However, this is not essential; sensible
defaults will be used for unspecified parameters, and they may be learned using
:func:`KalmanFilter.em`.
The figure drawn shows the true, hidden state, the state estimates given by the
Kalman Filter, and the state estimates given by the Kalman Smoother.
'''
import numpy as np
import pylab as pl
from pykalman import KalmanFilter

# specify parameters

Data =[np.array([ 5,  6,  7,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23], dtype=np.int32), 
np.array([8901482,  898952, 1107098,  554078,  365004,  427394,  406668,
        525004,  477256,  571558, 1107482,  909442,  784612,  696754,
   	    3112642, 3258892])]

measurements = [[5, 8901482], [6,898952], [7, 1107098], [9, 554078], [10,365004], [11,427394], [12, 406668], [13, 525004] , [14, 477256], [15,571558],[16,1107482],[17,909442],[18,784612],[19,696754],[20,3112642],[21,3258892]]

transition_matrix = [[1]]
transition_offset = [0.1]
observation_matrix = np.eye(1) + [[8901482]]
observation_offset = [1.0]
transition_covariance = np.eye(1)
observation_covariance = np.eye(1) + np.array([[1506519.875]])
initial_state_mean = [1827172.458]
initial_state_covariance = [[1]]

# sample from model
kf = KalmanFilter(
    transition_matrix, observation_matrix, transition_covariance,
    observation_covariance, transition_offset, observation_offset,
    initial_state_mean, initial_state_covariance,
    em_vars=[measurements]
)
states, observations = kf.sample(
    n_timesteps=24,
    initial_state=initial_state_mean
)

# estimate state with filtering and smoothing
filtered_state_estimates = kf.filter(observations)[0]
smoothed_state_estimates = kf.smooth(observations)[0]

# draw estimates


pl.figure()
pl.title('Predicted Data Usage over Time')
pl.xlabel('Time (hrs)')
pl.ylabel('Summed data usage (Mbbytes)')

lines_true = pl.plot(states, color='b')
lines_filt = pl.plot(filtered_state_estimates, color='b')
lines_smooth = pl.plot(smoothed_state_estimates, color='b')
pl.legend((lines_true[0], lines_filt[0], lines_smooth[0]),
          ('true', '', ''),
           loc='upper left'
)


pl.show()

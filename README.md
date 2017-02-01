# Datathon2016
Predictive Data Usage using Linear Prediction, Kalman Filter and PCR on CellTowers

## Table of Contents

 * Project Version
 * Dependencies
 * Introduction
 * Tutorial
 * Developer Documentation
 * Licenses 


##Project Version

## Dependencies
SciPy(and it's dependencies)
python 2.7
PyKalman


##Introduction

This is a basic to more advanced application of data usage on cell towers over time. Beginning with linear prediction, it uses the least squares method to predict how much data is being used in the proceeding days.

Using similar methodologies, we can use a Kalman filter to predict daily data usage.

Current time scale is daily, because the data is not granual enough and the recordings are not recorded on an even enough basis.

PCR and Kalman Filter are under development (PCR may be scraped for better methodologies)

##Tutorial



## Developer Documentation


### Maps

As dynamically generated as possible with matplotlib, maps.py generated a map with cell tower locations (as many as we can find), clicking on each cell point should launch dataprep


## Data conversion and merging
We take in two csv files, one being mobile_info and log_data and find where the corresponding device id use data on the cell tower. We sum that data over a 24hr period and place it into an array

From there, the data is graphed into matplot lib and displayed correspondingly.

### Prediction

Launched from Data_prep, Predicition uses a Kalman Filter to create a predicted flow of data over the same period of time. There should be three lines that show where the data is going.


## License
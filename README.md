# Datathon2016
Predictive Data Usage using Kalman Filter and PCR on CellTowers

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
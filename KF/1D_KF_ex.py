# ref: https://github.com/JustWon/kalman_filter_example/blob/master/1D_kalman_filter.py
# clone coding

from math import *
import matplotlib.pyplot as plt
import numpy as np

def initialize():
    mu = 0
    var = 3
    return mu, var

def Prediction(mu, var, control_input, control_var):
    pred_mu = mu + 1 * control_input
    pred_var = var + (control_input ** 2 * control_var)
    return pred_mu, pred_var 

def Correction(pred_mu, pred_var, measurement, measurement_var):
    k = pred_var / (pred_var + measurement_var)
    mu = pred_mu + k * (measurement - pred_mu)
    var = (1 - k) * pred_var
    return mu, var

def KalmanFilter(n):
    # Initialization
    mu, var = initialize()
    
    control_input = [1.7, 1.8, 1.5, 1.5, 1.3, 1.2, 1.0, 1.5, 1.3, 2.1]
    control_var = 3

    measurement = [1.0, 2.0, 3.5, 4.3, 4.9, 6.0, 7.0, 8.3, 8.8, 10.1]
    measurement_var = 3

    kalman = []

    for i in range(n):
        # Prediction Step
        pred_mu, pred_var = Prediction(mu, var, control_input[i], control_var)
        
        # Correction Step
        mu, var = Correction(pred_mu, pred_var, measurement[i], measurement_var)
        
        # Updated result
        kalman.append([mu, var])
    
    return kalman


if __name__ == "__main__":
    n = 10

    kalman = KalmanFilter(n)
    pose = []

    t = np.arange(0, n, 1)

    for i in range(len(kalman)):
        pose.append(kalman[i][0])
    
    print(kalman)
    plt.plot(t+1, pose, 'g^', markersize=10)
    plt.plot(t+1, t+1, 'bs', markersize=6)
    plt.show()

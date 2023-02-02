import pandas as pd
from math import *
import numpy as np
import matplotlib.pyplot as plt

PATH = "../../YDLidar-SDK/python_tutorials"
point_cloud_file_path = PATH + "/two_points.csv"


def CalculateSampleData():
    df = pd.read_csv(point_cloud_file_path)
    mean_ = df.groupby('Number').mean()
    rdata = []

    for i in range(5):
        rdata.append(mean_.iloc[i]['distance'] * 100)
    return rdata



def initialize():
    mu = 10
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
    
    control_input = [10.3, 10.2, 10.0, 9.7, 10.3]
    control_var = 3

    # measurement = [1.0, 2.0, 3.5, 4.3, 4.9, 6.0, 7.0, 8.3, 8.8, 10.1]
    measurement = CalculateSampleData()
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
    n = 5

    kalman = KalmanFilter(n)
    pose = []

    t = np.arange(20, 70, 10)

    for i in range(len(kalman)):
        pose.append(kalman[i][0])
    
    print(kalman)
    plt.plot(t+1, pose, 'g^', markersize=10)
    plt.plot(t+1, t, 'bs', markersize=6)
    plt.show()


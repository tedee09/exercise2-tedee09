import numpy as np
from question1 import get_DH_table 

def dh_transform(theta, d, a, alpha):
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def get_pos():
    dh = get_DH_table()
    
    T_final = np.eye(4)

    for joint in dh:
        theta, d, a, alpha = joint
        T = dh_transform(theta, d, a, alpha)
        T_final = np.dot(T_final, T)

    pos = T_final[:3, 3]
    
    return pos

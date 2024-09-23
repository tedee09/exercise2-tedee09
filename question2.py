import numpy as np
from question1 import get_DH_table  # Import DH table from question1.py

def dh_transform(theta, d, a, alpha):
    """
    This function returns the transformation matrix based on the DH parameters.
    """
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def get_pos():
    # Get the DH table from question1
    dh = get_DH_table()
    
    # Initialize the final transformation matrix as identity matrix
    T_final = np.eye(4)

    # Multiply transformation matrices for each joint
    for joint in dh:
        theta, d, a, alpha = joint
        T = dh_transform(theta, d, a, alpha)
        T_final = np.dot(T_final, T)

    # Extract the position of the end-effector (translation part)
    pos = T_final[:3, 3]
    
    return pos

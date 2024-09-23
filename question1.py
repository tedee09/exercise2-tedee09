import numpy as np

def get_DH_table():
    d1, d2, d3 = 0.7, 0.5, 0.3
    
    dh = np.array([
        [np.radians(45), d1, 0, np.radians(90)],   
        [np.radians(0), d2, 0, np.radians(0)],     
        [np.radians(90), d3, 0, np.radians(0)]     
    ])
    
    return dh

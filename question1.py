import numpy as np

def get_DH_table():
    d1, d2, d3 = 0.7, 0.5, 0.3
    
    dh = np.array([[0, d1, 0, -np.pi/2],  
                   [0, 0, d2, 0],       
                   [0, 0, d3, 0]])      
    
    return dh

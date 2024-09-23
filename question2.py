import numpy as np

def get_pos():
    dh_table = get_DH_table()  # Reuse the DH table from question1
    
    pos = np.zeros(3)
    
    for i in range(dh_table.shape[0]):
        theta = dh_table[i][0]
        d = dh_table[i][1]
        a = dh_table[i][2]
        
        pos[0] += a * np.cos(theta)  
        pos[1] += a * np.sin(theta)  
        pos[2] += d                 

    return pos

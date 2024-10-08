import numpy as np
from question1 import get_DH_table

def get_pos():
    dh_table = get_DH_table()
    
    pos = np.zeros(3)
    
    for i in range(dh_table.shape[0]):
        theta = dh_table[i][0]
        d = dh_table[i][1]
        a = dh_table[i][2]
        alpha = dh_table[i][3]
        
        # Calculate position contributions
        pos[0] += a * np.cos(theta)  # X position contribution from a
        pos[1] += a * np.sin(theta)  # Y position contribution from a
        pos[2] += d                  # Z position contribution from d

    return pos

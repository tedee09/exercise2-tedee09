import numpy as np
from question1 import get_DH_table

def get_pos(dh_table):
    pos = np.zeros(3)
    
    for i in range(dh_table.shape[0]):
        theta = dh_table[i][0]
        d = dh_table[i][1]
        a = dh_table[i][2]
        alpha = dh_table[i][3]
        
        # Hitung kontribusi posisi
        pos[0] += a * np.cos(np.radians(theta))  # Kontribusi X dari a
        pos[1] += a * np.sin(np.radians(theta))  # Kontribusi Y dari a
        pos[2] += d                              # Kontribusi Z dari d
    
    return pos

# Contoh penggunaan
dh_table = get_DH_table()
student_pos = get_pos(dh_table)

print("Posisi Akhir Efektor:", student_pos)

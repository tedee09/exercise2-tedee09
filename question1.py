import numpy as np

def get_DH_table():
    # Contoh parameter DH untuk robotic arm 3 DOF
    d1, d2, d3 = 70 mm, 50 mm, 30 mm  # Offset link dalam satuan mm
    a1, a2, a3 = 0 mm, 50 mm, 30 mm  # Panjang link dalam satuan mm
    alpha1, alpha2, alpha3 = -90 derajat, 0 derajat, 0 derajat  # Twist link dalam derajat
    theta1, theta2, theta3 = 45 derajat, 0 derajat, 90 derajat  # Sudut joint dalam derajat
    
    # Isi tabel DH
    dh_table = np.array([[theta1, d1/1000, a1/1000, alpha1],
                           [theta2, d2/1000, a2/1000, alpha2],
                           [theta3, d3/1000, a3/1000, alpha3]])
    
    return dh_table

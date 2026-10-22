import numpy as np
# Keyla Paola NC = 0033 | Fecha 22-oct-2026
n0033 = np.array([10,20,30,40,50])
print(n0033)
print(n0033[0])
print(n0033[3])
print(n0033[-1])
print(n0033[-2])
print("-----------------------")
n0033 = np.array([
    [10,20,30],
    [40,50,60]
])
print(n0033)
print(n0033[0, 0])
print(n0033[1, 2])
print(n0033[-1, -1])
print(n0033[-2, -2])
print("-----------------------")
# 3D array 
n0033 = np.array([
    [
      [10,20,30],
      [40,50,60]
],
[ 
      [70,80,90],
      [100,110,120]
    ]
])
print(n0033)
print(n0033[0,0,0])
print(n0033[1,1,2])
print(n0033[-1,-1,-2])
print("Keyla Paola NC = 0033 | Fecha 22-oct-2026")
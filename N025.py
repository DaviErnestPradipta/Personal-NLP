import numpy as np

def find_mag(array):
    mag = np.sqrt((array * array).sum())
    return mag

A = np.array([2, 5])
B = np.array([3, -2])

dot_product = A.dot(B)
A_mag = find_mag(A)
B_mag = find_mag(B)
cos = dot_product / (A_mag * B_mag)
print(f'{cos:.4f}')
import numpy as np

a = np.random.random((5, 5)) * 10
print(a)
print('---')
amin, amax = a.min(), a.max()
a = (a - amin) / (amax - amin)
print(a)

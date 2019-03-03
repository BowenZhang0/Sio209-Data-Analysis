import numpy as np

a = np.zeros((5))

for i in range (5):

    a[i] = input()
    
print(np.average(a))

import numpy as np
import math
b = np.arange(0,20,20/10, dtype=int)
print(type(b))
print(b)





def j(n, array):
    if n ==0:
        return  np.sin(array)/array
    elif n == 1:
        return  np.sin(array)/array**array -np.cos(array)/array
    elif n == 2:
        return  ((3/array*array - 1)*np.sin(array)/array - 3*np.cos(array)/array*array)
    else:
        raise ValueError
j(0, b)
import numpy as np

a = np.arange(0,9,dtype = np.uint8)
print(a,a.dtype)
b = a.astype(np.float32)
print(b,b.dtype)

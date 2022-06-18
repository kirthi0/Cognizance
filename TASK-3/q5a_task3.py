import numpy as np
m1 = np.random.randint(6 ,size = (2,3))
print("m1 =\n",m1)
m2 = np.random.randint(6 ,size = (3,5))
print("m2 =\n",m2)
m3 = np.dot(m1,m2)
print("m3 =\n",m3)
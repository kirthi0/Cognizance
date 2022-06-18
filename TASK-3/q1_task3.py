import numpy as np
print("Enter starting and ending numbers")
ni = int(input())
nend = int(input())
vector  = np.arange(ni,nend+1)
print(vector)
i = 5
new_vector = np.zeros(len(vector) + (len(vector)-1)*(i))
new_vector[::i+1] = vector
print("New Vector:")
print(new_vector)
import numpy as np
# creating a random vector of size 20 having only float in the range of 1-20
a = np.random.uniform(low=1,high=20, size=(1, 20))

print(a)
print("\n")
# reshaping the array to 4 by 5
a = a.reshape((4,5))

print(a)
print("\n")
# replacing the max in each row by 0
a = np.where(a == np.max(a, axis=1, keepdims=True), 0, a)
print(a)
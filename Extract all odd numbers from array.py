#Extract all odd numbers from array
import numpy as np
a=np.array([1,7,9,33,54,22,9,4])
odd=a[a%2==1]
print(odd)

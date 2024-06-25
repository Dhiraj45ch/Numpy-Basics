import numpy as np
a=np.array([1,3,12,43,34,21,92,4])

gr=np.extract(a>10,a)
print(gr)

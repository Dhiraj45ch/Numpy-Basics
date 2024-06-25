#WAP to create array elements between 25 to 45(10 elements).Arrange them in equal size array.

import numpy as np
ar=np.arange(25,45)
print (ar)
print("\n")

sub=np.split(ar,2)
for x in sub:
  print(x)

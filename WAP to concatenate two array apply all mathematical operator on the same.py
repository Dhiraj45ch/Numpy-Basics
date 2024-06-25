#WAP to concatenate two array apply all mathematical operator on the same

#WAP to concatenate two array
import numpy as np
a=np.array([1,3,12,43,34,21,92,4])
b=np.array([99,98])
c=np.concatenate((a,b)) 
print("Concatenate two array a and b= ",c)

#apply all mathematical operator on the same
add=c+2
sub=c-2
mul=c*2
div=c/2
print("add= ",add)
print("sub= ",sub)
print("mul= ",mul)
print("div= ",div)

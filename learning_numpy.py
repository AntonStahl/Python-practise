import numpy as np 

a = np.array([1, 2, 3])     #creates an array
print(type(a))              #prints "<class 'numpy.ndarray'>"
print(a.shape)              #prints "(3,)"   
print(a[0], a[1], a[2])     #prints "1 2 3"
a[0] = 5                    #changes an elemen of the array    
print(a)                    #prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]]) #rank 2 array
print(b.shape)                  #prints "(2, 3)"
print(b[0, 0],b[0, 1], b[1, 0]) #prints "1 2 4"



#array creating functions

c = np.zeros((2,2))
print(c)

d = np.ones((1,2))
print(d)

e = np.full((2,2), 7)
print(e)

f = np.eye(2)
print(f)

g = np.random.random((2,2))
print(g)
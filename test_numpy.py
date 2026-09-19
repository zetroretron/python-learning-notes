import numpy as np
'''

array= np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]],
                 [[1,2,3,4],[1,2,3,4],[1,2,3,4]],
                 [[1,2,3,4],[1,2,3,4],[1,2,3,4]]])

array= np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],
                 [1,2,3,4],[1,2,3,4],[1,2,3,4]])



word = array[0,0]+ array[2,0]
print(word)
'''



#slicing
'''
array= np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print(array[2:,0:2])
'''

#scalar arithmetic
'''
array = np.array([1,2,3])
print(array + 1)
'''
#vectorized math func
'''
array = np.array([1,2,3])
print(np.sqrt(array))

'''
'''
#Broadcasting
a1=np.array([[1,2,3,4],
             [5,6,7,8]])
a2=np.array([[1],[2],[3],[4]])
print(a1.shape)
print(a2.shape)
print(a1*a2)
'''

rng=np.random.default_rng()

print(rng.integers(low=1, high=100, size=(3,2))
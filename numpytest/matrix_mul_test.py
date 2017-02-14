import numpy as np

x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )

# z = [ [x11 * y11, x12 * y12], [x21 * y21, x22 * y22]
z = x * y
print(z)

'''
    2 3     1 2
    3 5     5 -1

    matrix1 * matrix2
    2*1 + 3 *5      2*2 + 3 * -1
    3 * 1+ 5 * 5    3 *2 + 5 * -1
'''
x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)))
z = x * y
print(z)


x = np.array( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)))
print(np.dot(x, y))
# elementary wise
z = np.multiply(x, y)
print(z)
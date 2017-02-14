import numpy as np

# http://scipy.github.io/old-wiki/pages/Numpy_Example_List
test_case = 3

if (test_case == 1):
    A = np.arange(3, 15).reshape(3, 4)
    for item in A:
        print(item)

    for item in A.flat:
        print(item)
elif test_case == 2:
    A = np.ones((2,2))
    B = np.random.randint(6, size =4).reshape(2,2)
    print(B)
    C = np.vstack((A, B))
    D = np.hstack((A, B))

    print(D)
elif test_case == 3:
    # to  vertical dimension
    A = np.array([1, 1, 1])[:, np.newaxis]

    B = np.array([2, 2, 2])[:, np.newaxis]
    D = np.hstack((A, B))
    print(type(D))
    print(D.shape)
    '''
        axis: 0 (row)
            |
            v

        axis :1 (column)
        ->
    '''

    E = np.append(D, np.array([
        [3],
        [3],
        [3]
    ]
    ), axis =1)
    print(type(E))
    print(E)


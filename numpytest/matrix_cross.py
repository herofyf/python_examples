import numpy as np

x = np.array([0,0,1])
y = np.array([0,1,0])

# formual 1: |a| . |b|.sin(x)

# formual 2:
'''
[        [              [
x1          x2              y1z2 - z1y2
y1    x     y2    =         z1x2 - x1z2
z1          z2              x1y2 - y1x2
]         ]                ]
'''
print(np.cross(x, y))
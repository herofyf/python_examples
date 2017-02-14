import matplotlib.pyplot  as plt
import numpy as np

fig,(ax) = plt.subplots(1,1)
#fig.add_subplot(1,2, 2)


import math
x= np.linspace(0, 2 * np.pi, 100).tolist()
y= [math.sin(item) for item in x ]


#ax.plot(x, y)


plt.xlabel('test')
plt.title("test title")
plt.show()


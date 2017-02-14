

# first you should have data with features(x, y). then with target(up part, down part)



# use svm to predict


# after got line parameters , how to draw the line

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)

y = 2 * x + 1

d = plt.plot(x, y, 'k-', label = 'non weighted div')
plt.legend()
plt.show()
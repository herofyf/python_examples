import matplotlib.pyplot  as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

N = 5
menMeans = [18, 35, 30, 35, 27]
menStd =   [2, 3, 4, 1, 2]
womenMeans = [25, 32, 34, 20, 25]
womenStd =   [3, 5, 2, 3, 3]

ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, menMeans, width,
                color ='black',
                yerr = menStd,
                error_kw=dict(elinewidth=2,ecolor='red')
                )

#ax.set_xlim(-width, len(ind) + width)
ax.set_ylim(0, 45)

ax.set_ylabel("Scores")
ax.set_title("score by group and gender")
xTickMarks = ['Group' + str(i) for i in range(1, 6)]
#ax.set_xticks(ind + width)
#xtickNames = ax.set_xticklabels(xTickMarks)
#plt.setp(xtickNames, rotation=45, fontsize = 10)

ax.legend((rects1[0],), ('Men',))
plt.show()


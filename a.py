import scipy as sp
import numpy as np
import sys, os

file_name = os.path.dirname(sys.argv[0])

file_name = file_name + "\C-067.txt"
data = sp.genfromtxt(file_name,
        delimiter="\t",
        skip_header=1,
        names = True,
        missing_values="INFINITE",
        filling_values= np.inf)
        
for row in data[:7]:
    print("{}\t{}".format(row['TK'], row['Cp']))
    print('...\t...')
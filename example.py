import numpy as np
import matplotlib.pyplot as plt

"""
This example plots a sin.  You should get a graph with a border all around, grey thin gridlines, and internal tick 
marks.
"""
from aiken_eng import plotting

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()

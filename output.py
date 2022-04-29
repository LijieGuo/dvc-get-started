import numpy as np

data = np.loadtxt("data.txt", delimiter=",")

np.savetxt("output.txt", data, delimiter=",", fmt="%d")
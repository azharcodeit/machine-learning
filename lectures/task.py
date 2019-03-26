import numpy as np
from matplotlib import pyplot as plt

labels, xs, ys = np.loadtxt("toy_data.csv", unpack= True)

data = np.vstack((xs,ys)).T

xs = data[:,0]
ys = data[:,1]


color = ["b" if label ==1 else "r" for label in labels]

plt.scatter(xs, ys, s=60, c=color)
plt.title('hypothesis and gradient descent')
plt.show()

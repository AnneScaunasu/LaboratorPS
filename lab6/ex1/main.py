import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def convolutie(x, h, m):
    y = []
    for n in range(len(x)):
        element = 0
        for k in range(m):
            element += x[k] * h[n-k]
        y.append(element)
    return y


r = np.random.rand(100)
t = np.arange(0,1,1/100)
fig, axs = plt.subplots(4)
fig.suptitle("Convolution")

axs[0].set_title("Original")
axs[0].plot(t,r)

r1 = convolutie(r,r,5)
axs[1].set_title("One convolution")
axs[1].plot(t,r1)

r2 = convolutie(r1,r1, 5)
axs[2].set_title("Two convolutions")
axs[2].plot(t,r2)

axs[3].set_title("Three convolutions")
axs[3].plot(t,convolutie(r2,r2,5))

plt.savefig("ex1a.pdf", format="pdf", bbox_inches="tight")
plt.show()

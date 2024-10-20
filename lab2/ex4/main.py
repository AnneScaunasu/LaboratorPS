import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

t = np.arange(0, 0.01, 1/8000)

si = np.sin(2 * 400 * np.pi * t + np.pi / 2)
st = 2 * (t * 400 - np.floor(t * 400 + 1 / 2))

fig, axs = plt.subplots(3)
fig.suptitle('Ex4')
axs[0].plot(t, si)
axs[1].plot(t, st)
axs[2].plot(t, si + st)

plt.savefig("ex4.pdf", format="pdf", bbox_inches="tight")
plt.show()

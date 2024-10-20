import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

t = np.arange(0,0.05,1/16000)
s = np.sin(600 * np.pi * t + np.pi/2)
c = np.cos(600 * np.pi * t)

fig, axs = plt.subplots(2)
fig.suptitle("Ex1")
axs[0].set_title("sin")
axs[0].plot(t, s)
axs[1].plot(t,c)
axs[1].set_title("cos")

plt.savefig("ex1.pdf",format="pdf",bbox_inches="tight")
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

t = np.arange(0, 1, 1/1000)
s = np.sin(2 * np.pi * 20 * t)

t1 = t[::4]
s1 = s[::4]

t2 = t1[1::3]
s2 = s1[1::3]

fig, axs = plt.subplots(3)
fig.suptitle("Ex7")
axs[0].stem(t, s)
axs[1].stem(t1, s1)
axs[2].stem(t2, s2)

plt.tight_layout()
plt.savefig("ex7.pdf",format="pdf",bbox_inches="tight")
plt.show()

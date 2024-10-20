import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

t = np.arange(0, 0.01, 1/8000)

a = np.sin(2 * np.pi * 4000 * t)
b = np.sin(2 * np.pi * 2000 * t)
c = np.sin(2 * np.pi * 0 * t)

fig, axs = plt.subplots(3)
fig.suptitle("Ex6")
axs[0].plot(t, a)
axs[1].plot(t, b)
axs[2].plot(t, c)

plt.savefig("ex6.pdf",format="pdf",bbox_inches="tight")
plt.show()

# din primul semnal nu se poate vedea ca este un semnal sinusoidal pentru ca nu pare uniforma partea de inceput cu cea de final
# din al doilea se poate intelege semnalul sinusoidal

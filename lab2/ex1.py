import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,1,0.0001)
sig_sin = 2 * np.sin(20 * np.pi * t + np.pi / 2)
sig_cos = 2 * np.cos(20 * np.pi * t)

fig, ass = plt.subplots(2)
fig.suptitle('Semnale identice')

ass[0].plot(t, sig_sin)
ass[0].set_title('sin(20tπ + π/2)')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')

ass[1].plot(t, sig_cos)
ass[1].set_title('cos(20tπ)')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')

plt.savefig("ex1.pdf", format="pdf", bbox_inches="tight")
plt.show()

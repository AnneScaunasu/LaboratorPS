import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.02, step = 1/16000)
a = np.cos(2 * np.pi * 400 * t)

c = (400 * t - np.floor(400 * t))

fig, ass = plt.subplots(3)
fig.suptitle('Merged signals')

ass[0].plot(t, a)
ass[0].set_title('cosine signal')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')


ass[1].plot(t, c)
ass[1].set_title('saw-tooth signal')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')


ass[2].plot(t, a+c)
ass[2].set_title('merged signal')
ass[2].set_xlabel('time')
ass[2].set_ylabel('amplitude')

plt.savefig("ex4.pdf", format="pdf", bbox_inches="tight")
plt.show()

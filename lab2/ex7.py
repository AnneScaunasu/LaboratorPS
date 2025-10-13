import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.5, step=1/500)
sig = np.cos(2 * np.pi * 435 * t + np.pi)

# a)

d_t = t[::4]
d_sig = sig[::4]

fig, ass = plt.subplots(2)
fig.suptitle('Decimated signal from first element')

ass[0].plot(t,sig)
ass[0].set_title('Original Signal')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')

ass[1].plot(d_t,d_sig)
ass[1].set_title('Decimated signal')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')

plt.savefig("ex7a.pdf", format="pdf", bbox_inches="tight")
plt.show()

# b)
d2_t = t[2::4]
d2_sig = sig[2::4]

fig1, ass1 = plt.subplots(2)
fig1.suptitle('Decimated signal from second element')

ass1[0].plot(t,sig)
ass1[0].set_title('Original Signal')
ass1[0].set_xlabel('time')
ass1[0].set_ylabel('amplitude')

ass1[1].plot(d2_t,d2_sig)
ass1[1].set_title('Decimated signal')
ass1[1].set_xlabel('time')
ass1[1].set_ylabel('amplitude')

plt.savefig("ex7b.pdf", format="pdf", bbox_inches="tight")
plt.show()

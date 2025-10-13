import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.05, step=1/1600)

a_sig = np.sin(2 * np.pi * 800 * t)
b_sig = np.sin(2 * np.pi * 400 * t)
c_sig = np.sin(2 * np.pi * 0 * t)

fig, ass = plt.subplots(3)
fig.suptitle('Frecvente fundamentale')

ass[0].plot(t,a_sig)
ass[0].set_title('fs/2')
ass[0].set_xlabel('time')
ass[0].set_ylabel('amplitude')

ass[1].plot(t,b_sig)
ass[1].set_title('fs/4')
ass[1].set_xlabel('time')
ass[1].set_ylabel('amplitude')

ass[2].plot(t,c_sig)
ass[2].set_title('0 Hz')
ass[2].set_xlabel('time')
ass[2].set_ylabel('amplitude')

plt.show()

import numpy as np
import matplotlib.pyplot as plt

fs = 4000
f0 = 121
t_tup_Nyquist = np.arange(0,0.05,1/4000)
signal_tup_1 = np.sin(2 * np.pi * f0 * t_tup_Nyquist)
signal_tup_2 = np.sin(2 * np.pi * (f0 + 1*fs) * t_tup_Nyquist)
signal_tup_3 = np.sin(2 * np.pi * (f0 + 2*fs) * t_tup_Nyquist)

t = np.arange(0,0.05,1/(fs*10))
signal_1 = np.sin(2 * np.pi * f0 * t)
signal_2 = np.sin(2 * np.pi * (f0 + 1*fs) * t)
signal_3 = np.sin(2 * np.pi * (f0 + 2*fs) * t)

fig, ass = plt.subplots(3)

ass[0].plot(t,signal_1)
ass[0].plot(t_tup_Nyquist, signal_tup_1, 'o', color='y')

ass[1].plot(t,signal_2)
ass[1].plot(t_tup_Nyquist, signal_tup_2, 'o', color='y')

ass[2].plot(t,signal_3)
ass[2].plot(t_tup_Nyquist, signal_tup_3, 'o', color='y')

plt.savefig(f"ex3.pdf", format="pdf", bbox_inches="tight")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

t_sub_Nyquist = np.arange(0,0.05,1/200)
signal_sub_1 = np.sin(2 * np.pi * 121 * t_sub_Nyquist)
signal_sub_2 = np.sin(2 * np.pi * (121 + 200) * t_sub_Nyquist)
signal_sub_3 = np.sin(2 * np.pi * (121 + 2*200) * t_sub_Nyquist)

t = np.arange(0,0.05,1/4000)
signal_1 = np.sin(2 * np.pi * 121 * t)
signal_2 = np.sin(2 * np.pi * (121 + 200) * t)
signal_3 = np.sin(2 * np.pi * (121 + 2*200) * t)

fig, ass = plt.subplots(3)

ass[0].plot(t,signal_1)
ass[0].plot(t_sub_Nyquist, signal_sub_1, 'o', color='y')

ass[1].plot(t,signal_2)
ass[1].plot(t_sub_Nyquist, signal_sub_2, 'o', color='y')

ass[2].plot(t,signal_3)
ass[2].plot(t_sub_Nyquist, signal_sub_3, 'o', color='y')

plt.savefig(f"ex2.pdf", format="pdf", bbox_inches="tight")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import math


def tf(ω, signal):
    tfω = 0
    for i in range(len(signal)):
        tfω += signal[i] * math.e**((1j * (-2) * np.pi * i * ω) / len(signal))
    return np.abs(tfω)


# Teo's discovery: The above function is highly volatile. If we give the function the 1/(step) to use instead of len(signal) it steadies itself
# We have realised after reading *more carefully* the course that the number of samples in the signal must be equal to the number of frequencies studied
# But this realization doesn't seem to fit Teo's solution and why does the result scale if we use (0,1600,2)?


t = np.arange(0,1,1/800)
sig_1 = 3.2 * np.cos(2 * np.pi * 150 * t)
sig_2 = 1.5 * np.cos(2 * np.pi * 300 * t)
sig_3 = 5 * np.cos(2 * np.pi * 100 * t)
ω = np.arange(0,800,1)
sig = sig_1 + sig_2 + sig_3
tf_sig = [tf(i,sig) for i in range(800)]

fig, ass = plt.subplots(1, 2)

ass[0].plot(t, sig)
ass[0].plot(t, sig_1, linestyle='dotted')
ass[0].plot(t, sig_2, linestyle='dotted')
ass[0].plot(t, sig_3, linestyle='dotted')
ass[0].set_xlabel('time')
ass[0].set_ylabel('x(t)')


ass[1].stem(ω[:len(ω)//2],tf_sig[:len(tf_sig)//2])
ass[1].set_xlabel('Frecventa')
ass[1].set_ylabel('|X(ω)|')

plt.savefig("ex3.pdf", format="pdf", bbox_inches="tight")
plt.show()

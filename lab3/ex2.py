import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.collections import LineCollection


def polar_sig_with_speed(sig, ω):
    return sig * math.e**(-2 * np.pi * 1j * ω * t)


t = np.arange(0,1,1/600)
sig = np.cos(2 * np.pi * 13 * t)
polar_sig = polar_sig_with_speed(sig,1)
polar_sig_2 = polar_sig_with_speed(sig,2)
polar_sig_7 =  polar_sig_with_speed(sig,7)
polar_sig_13 = polar_sig_with_speed(sig,13)

fig, (ass1, ass2) = plt.subplots(1,2, figsize=(8, 4))
fig.suptitle("Reprezentarea unui semnal in planul complex")

ass1.plot(t,sig)
ass1.set_xlabel('time')
ass1.set_ylabel('amplitude')

ass2.plot(polar_sig.real,polar_sig.imag)
ass2.set_xlabel('real')
ass2.set_ylabel('imaginar')

plt.savefig("ex2a.pdf", format="pdf", bbox_inches="tight")
plt.show()

fig, ass = plt.subplots(2,2)
fig.suptitle("Viteze diferite de infasurare")

ass[0,0].plot(polar_sig.real,polar_sig.imag)
ass[0,0].set_title('ω = 1')
ass[0,0].set_xlabel('real')
ass[0,0].set_ylabel('imaginar')

ass[0,1].plot(polar_sig_2.real,polar_sig_2.imag)
ass[0,1].set_title('ω = 2')
ass[0,1].set_xlabel('real')
ass[0,1].set_ylabel('imaginar')

ass[1,0].plot(polar_sig_7.real,polar_sig_7.imag)
ass[1,0].set_title('ω = 7')
ass[1,0].set_xlabel('real')
ass[1,0].set_ylabel('imaginar')

ass[1,1].plot(polar_sig_13.real,polar_sig_13.imag)
ass[1,1].set_title('ω = 13')
ass[1,1].set_xlabel('real')
ass[1,1].set_ylabel('imaginar')

plt.savefig("ex2b.pdf", format="pdf", bbox_inches="tight")
plt.show()

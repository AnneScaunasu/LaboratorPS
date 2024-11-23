import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def wrapped_signal(given_signal, omega, frequency):
    t_pi = np.linspace(0.0, 2 * np.pi, frequency)
    y_signal = given_signal * np.exp(1j * t_pi * omega)
    return np.real(y_signal), np.imag(y_signal)


t = np.arange(0,0.03, 0.00005)
signal = np.cos(2 * np.pi * 400 * t)

_, axs = plt.subplots(1,2)
axs[0].set_title("Plan real")
axs[0].plot(t,signal)

real_y, imaginary_y = wrapped_signal(signal, 1, int(0.03 / 0.00005))
axs[1].set_title("Plan imaginar")
axs[1].plot(real_y, imaginary_y)

plt.savefig("ex2-1.pdf", format="pdf", bbox_inches="tight")
plt.show()

real_2_y, imaginary_2_y = wrapped_signal(signal, 2, int(0.03 / 0.00005))
real_5_y, imaginary_5_y = wrapped_signal(signal, 5, int(0.03 / 0.00005))
real_7_y, imaginary_7_y = wrapped_signal(signal, 7, int(0.03 / 0.00005))

_, axs = plt.subplots(2,2)
axs[0][0].set_title("ω = 1")
axs[0][0].plot(real_y, imaginary_y)

axs[0][1].set_title("ω = 2")
axs[0][1].plot(real_2_y, imaginary_2_y)

axs[1][0].set_title("ω = 5")
axs[1][0].plot(real_5_y, imaginary_5_y)

axs[1][1].set_title("ω = 7")
axs[1][1].plot(real_7_y, imaginary_7_y)

plt.savefig("ex2-2.pdf", format="pdf", bbox_inches="tight")
plt.show()

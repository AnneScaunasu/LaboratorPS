import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


t = np.arange(0.0, 0.05, 0.00005)

sig_1 = np.cos(2 * np.pi * 500 * t)
sig_2 = np.cos(2 * np.pi * 100 * t)
sig_3 = np.cos(2 * np.pi * 320 * t)

signal = sig_1 + sig_2 + sig_3

fourier_values = []
frequencies = np.arange(0, 700, 20)

for m in range(700//20):
    fourier_value = 0
    for k in range(len(signal)):
        fourier_value += signal[k] * np.exp(-2 * np.pi * 1j * k * m / len(signal))
    fourier_values.append(np.abs(fourier_value))

fig, axs = plt.subplots(1,2)
axs[0].plot(t,signal)
axs[1].stem(frequencies, fourier_values)

plt.savefig("ex3.pdf", format="pdf", bbox_inches="tight")
plt.show()

from math import trunc

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

n = 8
timeline = [i for i in range(n)]
plot_matrix = [[[], []] for i in range(n)]
fourier_matrix = [[] for i in range(n)]

for line in range(n):
    for column in range(n):
        element = trunc(np.cos(2 * np.pi * line * column / n)) - 1j * trunc(np.sin(2 * np.pi * line * column / n))
        plot_matrix[line][0].append(element.real)
        plot_matrix[line][1].append(element.imag)
        fourier_matrix[line].append(element)

fig, axs = plt.subplots(n)
fig.suptitle("Fourier elements")
for line in range(n):
    axs[line].plot(timeline, plot_matrix[line][0], color="blue", label="real")
    axs[line].plot(timeline, plot_matrix[line][1], color="red", label="imaginary")

plt.savefig("ex1.pdf", format="pdf", bbox_inches="tight")
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

def verify_complex_unity(matrix):
    numpy_matrix = np.array(matrix)
    complex_conjugate = np.array(np.conjugate(numpy_matrix.T))
    return np.allclose(np.dot(numpy_matrix, complex_conjugate), np.identity(len(matrix)))

n = 8
timeline = [i for i in range(n)]
plot_matrix = [[[], []] for i in range(n)]
fourier_matrix = [[] for i in range(n)]

for line in range(n):
    for column in range(n):
        element = np.cos(2 * np.pi * line * column / n) - 1j * np.sin(2 * np.pi * line * column / n)
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

print(f"Is matix unit? {verify_complex_unity(fourier_matrix)}")

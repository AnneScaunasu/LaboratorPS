import matplotlib.pyplot as plt
import numpy as np
import math


def matrix_calc(n):
    return [[math.e**(-2 * np.pi * 1j * i * k / n) for k in range(n)] for i in range(n)]


def matrix_unity_calc(matrix):
    return np.allclose(np.dot(np.transpose(np.conjugate(matrix)), matrix), np.identity(len(matrix)))


fourier_matrix_8 = matrix_calc(8)
real_parts = []
imaginary_parts = []
timeline = [i for i in range(8)]
for i in range(len(fourier_matrix_8)):
    real_parts.append([fourier_matrix_8[i][j].real for j in range(len(fourier_matrix_8[i]))])
    imaginary_parts.append(([fourier_matrix_8[i][j].imag for j in range(len(fourier_matrix_8[i]))]))

fig, ass = plt.subplots(8)
for line in range(len(real_parts)):
    ass[line].plot(timeline, real_parts[line], color="green", label="real")
    ass[line].plot(timeline, imaginary_parts[line], color="purple", label="imaginary")

plt.savefig("ex1.pdf", format="pdf", bbox_inches="tight")
plt.show()

print(matrix_unity_calc(fourier_matrix_8))

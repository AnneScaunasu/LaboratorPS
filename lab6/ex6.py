import numpy as np
import matplotlib.pyplot as plt


values = [data[2] for data in np.genfromtxt('Train.csv', delimiter=',')]
values.pop(0)
N = len(values)

# a
# 10872
#  3 * 24 = 72
x = values[10872:10872 + 72]
plt.plot(x)
plt.title("Semnal original de 3 zile")
plt.savefig(f"ex6a.pdf", format="pdf", bbox_inches="tight")
plt.show()
plt.close()

# b
w = [5, 9, 13, 17]
plt.plot(x,label="Original signal")
plt.plot(np.convolve(x, np.ones(w[0]), 'valid') / w[0], label="w = 5")
plt.plot(np.convolve(x, np.ones(w[1]), 'valid') / w[1], label="w = 9")
plt.plot(np.convolve(x, np.ones(w[2]), 'valid') / w[2], label="w = 13")
plt.plot(np.convolve(x, np.ones(w[3]), 'valid') / w[3], label="w = 17")
plt.legend()
plt.savefig(f"ex6b.pdf", format="pdf", bbox_inches="tight")
plt.show()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

t = np.arange(0, 1, 1/1600)
a = np.sin(2 * 400 * np.pi * t)

plt.plot(t, a)
plt.stem(t, a)
plt.savefig("ex2a.pdf", format="pdf", bbox_inches="tight")
plt.show()

t = np.arange(0, 3, 1/200)
b = np.sin(2 * 800 * np.pi * t)

plt.plot(t, b)
plt.stem(t, b)
plt.savefig("ex2b.pdf", format="pdf", bbox_inches="tight")
plt.show()

t = np.arange(0, 0.05, 1/1600)
d = np.sign(np.sin(2 * 300 * np.pi * t))

plt.plot(t, d)
plt.stem(t, d)
plt.savefig("ex2d.pdf", format="pdf", bbox_inches="tight")
plt.show()

e = np.random.rand(128, 128)

plt.imshow(e)
plt.savefig("ex2e.pdf", format="pdf", bbox_inches="tight")
plt.show()

f = np.zeros((128,128))
for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        f[i, j] = i+j

plt.imshow(f)
plt.savefig("ex2f.pdf", format="pdf", bbox_inches="tight")
plt.show()


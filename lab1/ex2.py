import numpy as np
import matplotlib.pyplot as plt


ta = np.arange(0, 0.007, step = 1/1600)
a = np.cos(2 * np.pi * 400 * ta)
plt.plot(ta, a)
plt.stem(ta, a)
plt.savefig("ex2a.pdf", format="pdf", bbox_inches="tight")
plt.show()

tb = np.arange(0, 3, step = 1/1400)
b = np.cos(2 * np.pi * 800 * tb)
plt.plot(tb, b)
plt.savefig("ex2b.pdf", format="pdf", bbox_inches="tight")
plt.show()

tc = np.arange(0, 0.013, step = 1/16000)
c = (240 * tc - np.floor(240 * tc))
plt.plot(tc, c)
plt.savefig("ex2c.pdf", format="pdf", bbox_inches="tight")
plt.show()

td = np.arange(0, 0.05, step = 1/16000)
d = np.sign(np.cos(2 * np.pi * 300 * td))
plt.plot(td, d)
plt.savefig("ex2d.pdf", format="pdf", bbox_inches="tight")
plt.show()

e = np.random.rand(128,128)
plt.imshow(e)
plt.savefig("ex2e.pdf", format="pdf", bbox_inches="tight")
plt.show()

f = [[ np.cos(2*x) + np.sin(3*y) for x in range(128)] for y in range(128) ]
plt.imshow(f)
plt.savefig("ex2f.pdf", format="pdf", bbox_inches="tight")
plt.show()

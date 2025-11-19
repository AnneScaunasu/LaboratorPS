import numpy as np
import matplotlib.pyplot as plt


def reg_sig_constructor(i):
    if 34 < i < 64:
        return 1
    else:
        return 0


# a
N = 100
x1 = np.random.rand(N)
x2 = x1 * x1
x3 = x2 * x2
x4 = x3 * x3

fig, ass = plt.subplots(2,2)

ass[0,0].plot(x1)
ass[0,1].plot(x2)
ass[1,0].plot(x3)
ass[1,1].plot(x4)

plt.savefig(f"ex2a.pdf", format="pdf", bbox_inches="tight")
plt.show()
plt.close()

# esantioanele mai mici (comparate cu cele alaturate) sunt minimizate aproape spre 0

# b
reg_sig_1 = np.array([reg_sig_constructor(i) for i in range(100)])
reg_sig_2 = reg_sig_1 * reg_sig_1
reg_sig_3 = reg_sig_2 * reg_sig_2
reg_sig_4 = reg_sig_3 * reg_sig_3

fig, ass = plt.subplots(2,2)

ass[0,0].plot(reg_sig_1)
ass[0,1].plot(reg_sig_2)
ass[1,0].plot(reg_sig_3)
ass[1,1].plot(reg_sig_4)

plt.savefig(f"ex1b.pdf", format="pdf", bbox_inches="tight")
plt.show()

# semnalul ramane neschimbat

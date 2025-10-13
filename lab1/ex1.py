import numpy as np
import matplotlib.pyplot as plt


def get_signals(time):
    return (np.cos(520 * np.pi * time + np.pi / 3),
            np.cos(280 * np.pi * time - np.pi / 3),
            np.cos(120 * np.pi * time + np.pi / 3))


# x(t) = cos(520πt + π/3)
# y(t) = cos(280πt − π/3)
# z(t) = cos(120πt + π/3)

# a)
t = np.arange(0, 0.03, step = 0.00005)
print(t)

# b)
(x, y, z) = get_signals(t)

fig, axs = plt.subplots(3)
fig.suptitle('Semnale Continue Lab1-ex1')
axs[0].plot(t,x)
axs[1].plot(t,y)
axs[2].plot(t,z)

plt.savefig("ex1b.pdf", format="pdf", bbox_inches="tight")
plt.show()

# c)

n = np.arange(0, 0.03, step = 1/200)
print(n)

(xn, yn, zn) = get_signals(n)
fig, axs = plt.subplots(3)
fig.suptitle('Semnale Discrete Lab1-ex1')
axs[0].stem(n,xn)
axs[1].stem(n,yn)
axs[2].stem(n,zn)

plt.savefig("ex1c.pdf", format="pdf", bbox_inches="tight")
plt.show()

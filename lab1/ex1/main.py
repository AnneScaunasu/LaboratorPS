import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

def get_signals(time):
    return (np.cos(520 * np.pi * time + np.pi/3),
            np.cos(280 * np.pi * time - np.pi/3),
            np.cos(120 * np.pi * time + np.pi/3))

# x(t) = cos(520πt + π/3)
# y(t) = cos(280πt − π/3
# z(t) = cos(120πt + π/3)

t = np.arange(0,0.03,0.0005)

(x, y, z) = get_signals(t)

fig, axs = plt.subplots(3)
fig.suptitle('Ex1b')
axs[0].plot(t, x)
axs[1].plot(t, y)
axs[2].plot(t, z)

plt.savefig("ex1b.pdf", format="pdf", bbox_inches="tight")
plt.show()

t1 = np.arange(0,0.3,1/200)

(x1, y1, z1) = get_signals(t1)

fig, axs = plt.subplots(3)
fig.suptitle('Ex1c')
axs[0].stem(t, x1)
axs[0].set_title('x(t)')
axs[1].stem(t, y1)
axs[0].set_title('y(t)')
axs[2].stem(t, z1)
axs[0].set_title('z(t)')

plt.savefig("ex1c.pdf", format="pdf", bbox_inches="tight")
plt.show()

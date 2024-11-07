import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

t = np.arange(0,0.01, 100)
t_sin = []

for i in range(100):
    t_sin.append(i * np.pi / 100)

signal = np.cos(2 * np.pi * 400 * t)

fig, axs = plt.subplots(2)
axs[0].suptitle("Plan real")
axs[0].plot(t,signal)

axs[1].suptilte("Plan imaginar")
axs[1].plot(t_sin,)

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def snr_signal(vec, snr):
    z = np.random.normal(size=800)
    gamma = np.sqrt((np.linalg.norm(vec) ** 2) / ((np.linalg.norm(z) ** 2) * snr))
    return vec + gamma * z


t = np.arange(0,0.05,1/16000)
a = np.sin(300 * np.pi * t)
b = np.sin(300 * np.pi * t + np.pi / 4)
c = np.sin(300 * np.pi * t + 2 * np.pi / 4)
d = np.sin(300 * np.pi * t + 3 * np.pi / 4)

plt.plot(t,a, color='thistle')
plt.plot(t,b, color='plum')
plt.plot(t,c, color='violet')
plt.plot(t,d, color='mediumorchid')
plt.title("Ex2 - part 1")

plt.savefig("ex2-part1.pdf", format="pdf", bbox_inches="tight")
plt.show()

plt.plot(t,snr_signal(a, 0.1),label='SNR = 0.1', color='thistle')
plt.plot(t,snr_signal(a, 1),label='SNR = 1',color='plum')
plt.plot(t,snr_signal(a, 10),label='SNR = 10',color='violet')
plt.plot(t,snr_signal(a, 100),label='SNR = 100', color='mediumorchid')
plt.legend()
plt.title("Ex2 - part 2")
plt.savefig("ex2-part2.pdf", format="pdf", bbox_inches="tight")
plt.show()

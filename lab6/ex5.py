import numpy as np
import matplotlib.pyplot as plt


def fereastra_dreptunghiulara(N):
    # w(n) = 1
    return np.ones(N)


def fereastra_Hanning(N):
    # w(n) = 0.5[1 − cos( 2πn / N)]
    return np.array([0.5 * (1 - np.cos((2 * np.pi * n)/ N)) for n in range(N)])


dim = 200
t = np.arange(0, 0.05, 0.00001)
sig = np.sin(2 * np.pi * 100 * t)

fig, ass = plt.subplots(2,2)

ass[0,0].plot(t,sig)
ass[0,0].set_title("Semnal initial")

ass[0,1].plot(t, sig * np.pad(fereastra_dreptunghiulara(dim), ((len(sig)-dim)//2, (len(sig)-dim)//2),constant_values=0))
ass[0,1].set_title("Semnal filtrat printr-o fereastra dreptunghiulara")

ass[1,0].plot(t,sig)
ass[1,0].set_title("Semnal initial")

ass[1,1].plot(t, sig * np.pad(fereastra_Hanning(dim),((len(sig)-dim)//2, (len(sig)-dim)//2), constant_values=0))
ass[1,1].set_title("Semnal filtrat printr-o fereastra Hanning")

plt.savefig(f"ex5.pdf", format="pdf", bbox_inches="tight")
plt.show()

import numpy as np
import matplotlib.pyplot as plt


n = np.arange(0, 1, 1/64)

sig1 = [[np.sin(2 * np.pi * n1 + 3 * np.pi * n2) for n1 in n] for n2 in n]
sig2 = [[np.sin(4 * np.pi * n1) + np.cos(6 * np.pi * n2) for n1 in n] for n2 in n]

fig, ass = plt.subplots(2,2)

ass[0,0].imshow(sig1)
ass[0,0].set_title("original signal 1")
ass[0,1].imshow((20 * np.log10(abs(np.fft.fft2(sig1)))), cmap='viridis')
ass[0,1].set_title("fft signal 1")

ass[1,0].imshow(sig2)
ass[1,0].set_title("original signal 2")
ass[1,1].imshow((20 * np.log10(abs(np.fft.fft2(sig2)))), cmap='viridis')
ass[1,1].set_title("fft signal 2")

plt.savefig(f"ex1a.pdf", format="pdf", bbox_inches="tight")
plt.show()

fft1 = np.zeros((64,64))
fft1[0,5] = 1
fft1[0, 64 - 5] = 1

fft2 = np.zeros((64,64))
fft2[5,0] = 1
fft2[64-5,0] = 1

fft3 = np.zeros((64,64))
fft3[5,5] = 1
fft3[64-5,64-5] = 1

fig, ass = plt.subplots(3,2)
ass[0,0].imshow(fft1)
ass[0,0].set_title("fft 1")
ass[0,1].imshow(np.real(np.fft.ifft2(fft1)))
ass[0,1].set_title("signal 1")

ass[1,0].imshow(fft2)
ass[1,0].set_title("fft 2")
ass[1,1].imshow(np.real(np.fft.ifft2(fft2)))
ass[1,1].set_title("signal 2")

ass[2,0].imshow(fft3)
ass[2,0].set_title("fft 3")
ass[2,1].imshow(np.real(np.fft.ifft2(fft3)))
ass[2,1].set_title("signal 3")

plt.savefig(f"ex1b.pdf", format="pdf", bbox_inches="tight")
plt.show()

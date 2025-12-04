import numpy as np
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


img = rgb2gray(data.cat())
fft_img = np.fft.fft2(img)
freq_img = 20 * np.log10(abs(fft_img))

# ex lab
#
# freq_cutoff = 40
# fft_cutoff = fft_img.copy()
# fft_cutoff[freq_img > freq_cutoff] = 0
# img_cutoff = np.fft.ifft2(fft_cutoff)
# img_cutoff = np.real(img_cutoff)
#
# plt.imshow(img_cutoff, cmap="gray")
# plt.show()

# 2
set_snr = 20

mag = np.sort(np.abs(fft_img).flatten())[::-1]
e_total = np.sum(mag**2)
e_lost = np.cumsum((mag[::-1])**2)

val_snr = 10 * np.log10(e_total/e_lost)
idx = np.where(val_snr >= set_snr)[0][-1]
cutoff = 20 * np.log10(mag[len(mag) - 1 - idx])

fft_cutoff = fft_img.copy()
fft_cutoff[np.abs(fft_cutoff) < cutoff] = 0
img_cutoff = np.fft.ifft2(fft_cutoff)
img_cutoff = np.real(img_cutoff)

plt.imshow(img_cutoff, cmap="gray")
plt.savefig("ex2.pdf", format="pdf", bbox_inches="tight")
plt.show()

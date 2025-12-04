import scipy
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np


img = rgb2gray(data.cat())

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.savefig(f"pic.pdf", format="pdf", bbox_inches="tight")

plt.show()

fft_img = 20 * np.log10(abs(np.fft.fft2(img)))

plt.imshow(fft_img)
plt.colorbar()
plt.savefig(f"fft_pic.pdf", format="pdf", bbox_inches="tight")
plt.show()

rotate_angle = 45
img45 = scipy.ndimage.rotate(img, rotate_angle)
plt.imshow(img45, cmap='gray')
plt.savefig(f"rotated_pic.pdf", format="pdf", bbox_inches="tight")
plt.show()

fft_image45 = 20 * np.log10(abs(np.fft.fft2(img45)))
plt.imshow(fft_image45)
plt.colorbar()
plt.savefig(f"fft_rotated_pic.pdf", format="pdf", bbox_inches="tight")
plt.show()

freq_x = np.fft.fftfreq(img.shape[1])
freq_y = np.fft.fftfreq(img.shape[0])

plt.stem(freq_x, fft_img[:][0])
plt.savefig(f"fft_pic_freq.pdf", format="pdf", bbox_inches="tight")
plt.show()

freq_cutoff = 40

Y_cutoff = img.copy()
Y_cutoff[fft_img > freq_cutoff] = 0
X_cutoff = np.fft.ifft2(Y_cutoff)
X_cutoff = np.real(X_cutoff)
plt.imshow(X_cutoff, cmap='gray')
plt.savefig(f"pic_cutoff.pdf", format="pdf", bbox_inches="tight")
plt.show()

pixel_noise = 50

noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=img.shape)
X_noisy = img + noise
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.show()
plt.imshow(X_noisy, cmap='gray')
plt.title('Noisy')
plt.savefig(f"noisy_pic.pdf", format="pdf", bbox_inches="tight")
plt.show()

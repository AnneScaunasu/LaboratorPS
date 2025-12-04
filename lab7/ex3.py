import numpy as np
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


def snr(original, noisy):
    noise = original - noisy
    return 10 * np.log10(np.sum(original**2) / np.sum(noise**2))


img = rgb2gray(data.cat())
fft_img = np.fft.fft2(img)
freq_img = 20 * np.log10(abs(fft_img))

pixel_noise = 0.5

noise = np.random.uniform(-pixel_noise, high=pixel_noise, size=img.shape)
img_noisy = np.clip(img + noise, 0, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.show()
plt.imshow(img_noisy, cmap='gray')
plt.title('Noisy')
plt.show()

first_snr = snr(img, img_noisy)
fft_noisy = np.fft.fft2(img_noisy)

mag = np.sort(np.abs(fft_noisy).flatten())[::-1]
e_total = np.sum(mag**2)
e_lost = np.cumsum((mag[::-1])**2)

val_snr = 10 * np.log10(e_total / e_lost)
idx = np.where(val_snr >= first_snr + 5)[0][-1]
cutoff = mag[len(mag) - 1 - idx]

fft_noisy_cutoff = fft_noisy.copy()
fft_noisy_cutoff[np.abs(fft_noisy_cutoff) < cutoff] = 0
noisy_img_cutoff =np.fft.ifft2(fft_noisy_cutoff)
noisy_img_cutoff = np.real(noisy_img_cutoff)

second_snr = snr(img, noisy_img_cutoff)

fig, ass = plt.subplots(3)

ass[0].imshow(img, cmap='gray')
ass[0].set_title('Original')

ass[1].imshow(img_noisy, cmap='gray')
ass[1].set_title('Noisy')

ass[2].imshow(noisy_img_cutoff, cmap='gray')
ass[2].set_title('After filter')

plt.savefig("ex3.pdf", format="pdf", bbox_inches="tight")
plt.show()

print(f"SNR înainte: {first_snr:.2f} dB")
print(f"SNR după: {second_snr:.2f} dB")

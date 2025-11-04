import numpy as np
import matplotlib.pyplot as plt
import scipy


# a
rate, x = scipy.io.wavfile.read('vocale.wav')

# b
sound_groups = [x[i:(i + int(len(x) * 0.01))] for i in np.arange(0,len(x) - int(len(x) * 0.01),int(len(x) * 0.005))]

# c + d
fft_groups = np.array([np.abs(np.fft.fft(sound_groups[i])) for i in range(len(sound_groups))]).transpose()

# e

# P ∝ A^2
# Ldb = 10 * log10(P/Pref)
# Ldb = 10 * log10(A^2) = 20 * log10(A)

plt.imshow(20*np.log10(fft_groups[:len(fft_groups)//2, :]),
           aspect='auto',
           origin='lower',
           cmap='plasma',
           extent=(0, len(x)/rate, 0, rate/2))

plt.savefig(f"ex6.pdf", format="pdf", bbox_inches="tight")
plt.show()

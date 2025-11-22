import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

values = [data[2] for data in np.genfromtxt('Train.csv', delimiter=',')]
values.pop(0)
N = len(values)

# a)
# 10872
#  3 * 24 = 72
x = values[10872:10872 + 72]
plt.plot(x)
plt.title("Semnal original de 3 zile")
plt.savefig(f"ex6a.pdf", format="pdf", bbox_inches="tight")
plt.show()
plt.close()

# b)
w = [5, 9, 13, 17]
plt.plot(x,label="Original signal")
plt.plot(np.convolve(x, np.ones(w[0]), 'valid') / w[0], label="w = 5")
plt.plot(np.convolve(x, np.ones(w[1]), 'valid') / w[1], label="w = 9")
plt.plot(np.convolve(x, np.ones(w[2]), 'valid') / w[2], label="w = 13")
plt.plot(np.convolve(x, np.ones(w[3]), 'valid') / w[3], label="w = 17")
plt.legend()
plt.savefig(f"ex6b.pdf", format="pdf", bbox_inches="tight")
plt.show()

# c)
# so with some online ;) help:
# we can look at the patters as 'cycles'
# a daily cycle => 24h => 1/24 = 0.041[6] cycles/hour
# a weekly cycle => 24 * 7 = 168h => 1/168 = 0.00595 cycles/hour
# We want to keep these trends in the signal so we choose a cut-off frequency above these two
#  0.05 cycles / hour => 0.05/3600 => 1 / 72000 Hz
# Nyquist frequency = fs / 2 = 1 / 3600 / 2 = 1 / 7200z
# => cut-off frequency => 7200 / 72000 => 0.1

# d)
b_butter, a_butter = signal.butter(5, 0.1, btype='low')
b_cheby, a_cheby = signal.cheby1(5, 5, 0.1, btype='low')

# e)
plt.plot(x,label="Original signal")
plt.plot(signal.filtfilt(b_butter, a_butter, x), label="Butterworth Filter")
plt.plot(signal.filtfilt(b_cheby, a_cheby, x), label="Chebyshev Filter")
plt.legend()
plt.savefig(f"ex6e.pdf", format="pdf", bbox_inches="tight")
plt.show()

# f)
b_butter_sm, a_butter_sm = signal.butter(2, 0.1, btype='low')
b_cheby_sm, a_cheby_sm = signal.cheby1(2, 5, 0.1, btype='low')

b_butter_bg, a_butter_bg = signal.butter(8, 0.1, btype='low')
b_cheby_bg, a_cheby_bg = signal.cheby1(8, 5, 0.1, btype='low')

plt.plot(x,label="Original signal")
plt.plot(signal.filtfilt(b_butter_sm, a_butter_sm, x), label="Butterworth Filter with N=2")
plt.plot(signal.filtfilt(b_butter, a_butter, x), label="Butterworth Filter with N=5")
plt.plot(signal.filtfilt(b_butter_bg, a_butter_bg, x), label="Butterworth Filter  with N=8")
plt.plot(signal.filtfilt(b_cheby_sm, a_cheby_sm, x), label="Chebyshev Filter with N=2")
plt.plot(signal.filtfilt(b_cheby, a_cheby, x), label="Chebyshev Filter with N=5")
plt.plot(signal.filtfilt(b_cheby_bg, a_cheby_bg, x), label="Chebyshev Filter with N=8")
plt.legend()
plt.savefig(f"ex6f1.pdf", format="pdf", bbox_inches="tight")
plt.show()
plt.close()


b_cheby_0_5, a_cheby_0_5 = signal.cheby1(5, 0.5, 0.1, btype='low')
b_cheby_2_5, a_cheby_2_5 = signal.cheby1(5, 2.5, 0.1, btype='low')
b_cheby_10, a_cheby_10 = signal.cheby1(5, 10, 0.1, btype='low')

plt.plot(x,label="Original signal")
plt.plot(signal.filtfilt(b_cheby_0_5, a_cheby_0_5, x), label="Chebyshev Filter with rp=0.5dB")
plt.plot(signal.filtfilt(b_cheby_2_5, a_cheby_2_5, x), label="Chebyshev Filter with rp=2.5dB")
plt.plot(signal.filtfilt(b_cheby, a_cheby, x), label="Chebyshev Filter with rp=5dB")
plt.plot(signal.filtfilt(b_cheby_10, a_cheby_10, x), label="Chebyshev Filter with rp=10dB")
plt.legend()
plt.savefig(f"ex6f2.pdf", format="pdf", bbox_inches="tight")
plt.show()

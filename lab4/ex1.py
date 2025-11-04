import time

import numpy as np
import matplotlib.pylab as plt
import math


def dtf(ω, signal):
    tfω = 0
    for i in range(len(signal)):
        tfω += signal[i] * math.e**((1j * (-2) * np.pi * i * ω) / len(signal))
    return np.abs(tfω)


# def fft(m, signal):
#     N = len(signal)
#     if N == 1:
#         return signal[0]
#     elif not math.log2(N).is_integer():
#         raise Exception('The given signal has a length that is not a power of two!')
#
#     return fft(m, signal[::2]) + (math.e ** (-2 * np.pi * 1j * m / N)) * fft(m, signal[1::2])


def fft(signal):
    N = len(signal)
    if N == 1:
        return signal[0]
    elif not math.log2(N).is_integer():
        raise Exception('The given signal has a length that is not a power of two!')

    even = fft(signal[::2])
    odd = fft(signal[1::2])

    k = np.arange(N // 2)
    expo = math.e ** (-2 * 1j * np.pi * k / N)

    return np.concatenate([even + expo * odd, even - expo * odd])




totalN = [128, 256, 512, 1024, 2048, 4096, 8192]

my_times_dft = []
my_times_fft = []
numpy_times = []

for n in totalN:
    fig, ass = plt.subplots(1,3)


    t = np.arange(0,1,1/n)
    signal = np.cos(2 * np.pi * 250 * t) + np.cos(2 * np.pi * 75 * t)
    # my version dft
    my_start_time_dft = time.time_ns()
    ω = np.arange(0, n, 1)
    tf_sig = [dtf(i,signal) for i in range(n)]
    my_end_time_dft = time.time_ns()
    my_time_dft = my_end_time_dft - my_start_time_dft

    # my plot dft
    ass[0].stem(ω[:len(ω)//2],np.real(tf_sig[:len(tf_sig)//2]))
    ass[0].set_xlabel('Frecventa')
    ass[0].set_ylabel('|X(ω)|')
    ass[0].set_title('DFT')

    # my version fft
    my_start_time_fft = time.time_ns()
    ω = np.arange(0, n, 1)
    tf_sig = fft(signal)
    my_end_time_fft = time.time_ns()
    my_time_fft = my_end_time_fft - my_start_time_fft

    # my plot fft
    ass[1].stem(ω[:len(ω)//2],np.real(tf_sig[:len(tf_sig)//2]))
    ass[1].set_xlabel('Frecventa')
    ass[1].set_ylabel('|X(ω)|')
    ass[1].set_title('FFT')

    # numpy
    numpy_start_time = time.time_ns()
    np_fft = np.fft.fft(signal,n)
    numpy_end_time = time.time_ns()
    np_time = numpy_end_time - numpy_start_time

    # numpy plot
    ass[2].plot(np.real(np_fft[:len(np_fft)//2]))
    ass[2].set_xlabel('Frecventa')
    ass[2].set_ylabel('|X(ω)|')
    ass[2].set_title('Numpy FFT')

    # recording time and saving the files
    my_times_dft.append(my_time_dft)
    my_times_fft.append(my_time_fft)
    numpy_times.append(np_time)

    plt.savefig(f"fourier_graphs/ex1-{n}.pdf", format="pdf", bbox_inches="tight")
    plt.close()
    print(f"Finished {n}")

plt.figure()
plt.plot(totalN, np.log(my_times_dft),label="My DFT")
plt.plot(totalN, np.log(my_times_fft),label="My FFT")
# numpy time usually is 0 and the function fails because it can't do log(0)
# plt.plot(totalN, np.log(numpy_times),label="Numpy FFT")
plt.xlabel("N")
plt.ylabel("log(Time)")
plt.title("Execution Time Comparison")
plt.legend()

plt.savefig(f"ex1-times.pdf", format="pdf", bbox_inches="tight")
plt.show()

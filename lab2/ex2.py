import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal


def transform_signal_for_snr(signal, noise_signal, snr):
    # SNR = ||sig||^2 / (γ^2 * ||z||^2) => γ = root(||sig||^2 / (snr * ||z||^2))
    # gamma = np.power(np.power(np.linalg.norm(signal),2) / (snr * np.power(np.linalg.norm(noise_signal),2)),1/2)
    gamma = np.power(np.sum(np.power(np.linalg.norm(signal), 2)) / (snr * np.sum(np.power(np.linalg.norm(noise_signal), 2))), 1 / 2)
    print()
    print(signal + gamma * noise_signal)
    return signal + gamma * noise_signal


t = np.arange(0,0.01,0.0001)
sig_1 = np.cos(2 * np.pi * 240 * t)
sig_2 = np.cos(2 * np.pi * 240 * t + np.pi / 2)
sig_3 = np.cos(2 * np.pi * 240 * t + 2 * np.pi / 2)
sig_4 = np.cos(2 * np.pi * 240 * t + 3 * np.pi / 4)

fig, ass = plt.subplots(2,2)
fig.suptitle('Different phases same signal')

ass[0,0].plot(t,sig_1)
ass[0,0].set_title('phase 0')
ass[0,0].set_xlabel('time')
ass[0,0].set_ylabel('amplitude')

ass[0,1].plot(t,sig_2)
ass[0,1].set_title('phase π/2')
ass[0,1].set_xlabel('time')
ass[0,1].set_ylabel('amplitude')

ass[1,0].plot(t,sig_3)
ass[1,0].set_title('phase π')
ass[1,0].set_xlabel('time')
ass[1,0].set_ylabel('amplitude')

ass[1,1].plot(t,sig_4)
ass[1,1].set_title('phase 3π/4')
ass[1,1].set_xlabel('time')
ass[1,1].set_ylabel('amplitude')


plt.savefig("ex2a.pdf", format="pdf", bbox_inches="tight")
plt.show()


# b)

noisy_signal_1 = transform_signal_for_snr(sig_1, np.random.normal(size=len(t)), 0.1)
noisy_signal_2 = transform_signal_for_snr(sig_1, np.random.normal(size=len(t)), 1)
noisy_signal_3 = transform_signal_for_snr(sig_1, np.random.normal(size=len(t)), 10)
noisy_signal_4 = transform_signal_for_snr(sig_1, np.random.normal(size=len(t)), 100)

fig, ass = plt.subplots(2,2)
fig.suptitle('Noisy signals depending on SNR')

ass[0,0].plot(t,noisy_signal_1)
ass[0,0].set_title('SNR = 0.1')
ass[0,0].set_xlabel('time')
ass[0,0].set_ylabel('amplitude')

ass[0,1].plot(t,noisy_signal_2)
ass[0,1].set_title('SNR = 1')
ass[0,1].set_xlabel('time')
ass[0,1].set_ylabel('amplitude')

ass[1,0].plot(t,noisy_signal_3)
ass[1,0].set_title('SNR = 10')
ass[1,0].set_xlabel('time')
ass[1,0].set_ylabel('amplitude')

ass[1,1].plot(t,noisy_signal_4)
ass[1,1].set_title('SNR = 100')
ass[1,1].set_xlabel('time')
ass[1,1].set_ylabel('amplitude')

plt.savefig("ex2b.pdf", format="pdf", bbox_inches="tight")
plt.show()

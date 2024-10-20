import scipy
import matplotlib
import numpy as np
import sounddevice as sd
matplotlib.use('TkAgg')

sd.default.samplerate = 44100

t = np.arange(0, 5, 1/8000)
a = np.sin(2 * 400 * np.pi * t)
sd.play(a)
sd.wait()

t = np.arange(0, 3, 1/8000)
b = np.sin(2 * 800 * np.pi * t)
sd.play(b)
sd.wait()

t = np.arange(0, 5, 1/8000)
d = np.sign(np.sin(2 * 300 * np.pi * t))
sd.play(d)
sd.wait()

rate = int(10e5)
scipy.io.wavfile.write('ex3.wav', rate, a)
rate, x = scipy.io.wavfile.read('ex3.wav')
sd.play(x)
sd.wait()

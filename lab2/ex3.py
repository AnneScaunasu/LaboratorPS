import numpy as np
import sounddevice as sd
import scipy

ta = np.arange(0, 3, step = 1/160000)
a = np.cos(2 * np.pi * 400 * ta)
sd.play(a)
sd.wait()

tb = np.arange(0, 3, step = 1/140000)
b = np.cos(2 * np.pi * 800 * tb)
sd.play(b)
sd.wait()

tc = np.arange(0, 3, step = 1/16000)
c = (240 * tc - np.floor(240 * tc))
sd.play(c)
sd.wait()

td = np.arange(0, 3, step = 1/16000)
d = np.sign(np.cos(2 * np.pi * 200 * td))
sd.play(d)
sd.wait()

rate = int(10e5)
scipy.io.wavfile.write('signal_sound.wav', rate, d)
rate, x = scipy.io.wavfile.read('signal_sound.wav')
sd.play(x, 44100)
sd.wait()

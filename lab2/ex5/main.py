import matplotlib
import numpy as np
import sounddevice as sd
matplotlib.use('TkAgg')

t = np.arange(0, 5, 1/8000)

x1 = np.sin(2 * 360 * np.pi * t)
x2 = np.sin(2 * 512 * np.pi * t)

sd.play(np.concatenate((x1, x2)), 44100)
sd.wait()

# se aude ca al doilea este la o frecventa mai inalta

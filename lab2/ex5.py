import sounddevice as sd
import numpy as np

t = np.arange(0, 3, step=1/160000)
small_sig = np.cos(2 * np.pi * 300 * t)
big_sig = np.cos(2 * np.pi * 540 * t)
sd.play(np.concatenate([small_sig, big_sig]))
sd.wait()

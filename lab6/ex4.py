import numpy as np


def rezultatul_teoremei_de_deplasare(x, y):
    return np.fft.ifft(
        np.conjugate(np.fft.fft(x)) * np.fft.fft(y)
    )


def rezultatul_teoremei_de_deplasare_cu_impartire(x,y):
    return np.fft.ifft(
        np.fft.fft(y) / np.fft.fft(x)
    )


x = np.random.rand(20)
d = 6
y = np.roll(x, d)

print(f"Rezultatul Teoriei de Deplasare este: \n {rezultatul_teoremei_de_deplasare(x,y)}")
print(f"Rezultatul Teoriei de Deplasare prin impartire: \n {rezultatul_teoremei_de_deplasare_cu_impartire(x,y)}")

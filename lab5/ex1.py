import numpy as np
import matplotlib.pyplot as plt


def sort_after_biggest_fft_value(pair_fft_freq):
    return pair_fft_freq[0]


values = [data[2] for data in np.genfromtxt('Train.xls', delimiter=',')]
values.pop(0)
N = len(values)

# a) 1/ora = 1/(60*60) = 1/3600 Hz
# b) prima: 0,25-08-2012 00:00,8
# ultima: 18287,25-09-2014 23:00,534
# interval: 2 ani, 1 luna, 23 ore sau 18288 * 1 ora => 18288 ore
# c) Frecventa maxima posibila este fs/2 => 1/5200 Hz
# d)
data_fft_abs = np.abs(np.fft.fft(values)/N)
f = 1/3600 * np.linspace(0, N//2, N//2)/N

plt.stem(f,data_fft_abs[:N//2])
plt.xlabel('Frecventa [Hz]')
plt.ylabel('|FFT(ω)|')
plt.savefig(f"ex1d.pdf", format="pdf", bbox_inches="tight")
plt.show()

# e) Da, semnalul prezinta o componenta continua; transformata Fourier are o valoare semnificativa pentru frecventa 0Hz
processed_data = values - np.average(values)
processed_data_fft = np.abs(np.fft.fft(processed_data)/N)

plt.stem(f,processed_data_fft[:N//2])
plt.xlabel('Frecventa [Hz]')
plt.ylabel('|FFT(ω)|')
plt.savefig(f"ex1e.pdf", format="pdf", bbox_inches="tight")
plt.show()

# f)
processed_fft_freq_pairs = []
for i in range(len(processed_data_fft[:N//2])):
    processed_fft_freq_pairs.append((processed_data_fft[i], f[i]))

sorted_processed_fft_freq_pairs = sorted(processed_fft_freq_pairs,key=sort_after_biggest_fft_value,reverse=True)

for i in range(4):
    print(f"Frecventa { i + 1 } este {sorted_processed_fft_freq_pairs[i][1]}")

# g
# 10464 -> luni 04.11.2013
# o luna de esantioane, aproximam 30 de zile => 30 * 24 = 720 esantioane
luna_esantionare = values[10464:11184]

plt.plot(luna_esantionare)
plt.title("Luna de esantionare din 04.11.2013")
plt.savefig(f"ex1g.pdf", format="pdf", bbox_inches="tight")
plt.show()

# h
plt.plot(values)
plt.show()
# dupa cum s-a mentionat in timpul laboratorului oamenii au tendinte periodice
# daca analizam in timp semnalul putem observa:
#   - un trend continuu ascendent apoi direct descendent care face diserenta intre zi si noapte
#   - mai putem observa si dupa fiecare grup de 5 inregistrari relativ inalte in timpul zilei, 2 grupuri care sunt mai
#       joase decat cele de inaintea lor care inca zilele saptamanii si weekend-urile

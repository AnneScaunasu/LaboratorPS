from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

def isInArray(n, a):
    for p in a:
        if p[0] == n:
            return True
    return False


# a) 1/ora => f0 = 1/3600
# b) 18288 ore => 762 zile
# c) 1244
# d)
x = np.genfromtxt('Train.xls', delimiter=',', skip_header=1)[:, 2]
fft = np.abs(np.fft.fft(x)) / len(x)

freq = 1 / 3600 * np.linspace(0, len(x) // 2, num = len(x) // 2)
plt.plot(freq, fft[:len(x) // 2])
plt.savefig("ex1d.pdf", format="pdf", bbox_inches="tight")
plt.show()

# e) Media semnalului este diferita de 0 deci semnalul are o componenta continua
fftwdc = np.abs(np.fft.fft(x - np.mean(x))) / len(x)
plt.plot(freq, fftwdc[:len(x) // 2])
plt.savefig("ex1e.pdf", format="pdf", bbox_inches="tight")
plt.show()

# f)
max_count = 4
max_arr = []

while max_count != 0:
    last_max = 0
    freq_last_max = -1
    for p in range(len(fft[:len(x) // 2])):
        if (fft[p] > last_max and max_count == 4) or (last_max < fft[p] and not isInArray(fft[p],max_arr)):
            last_max = fft[p]
            freq_last_max = freq[p]
    max_arr.append((last_max,freq_last_max))
    max_count -= 1

for p in max_arr:
    print(p)

# g)
es = np.genfromtxt('Train.csv', delimiter=',', dtype=None, names=True, encoding = 'utf-8')[1000:]
firstMondayPosition = -1
# find first Monday
for p in range(len(es)):
    if datetime.strptime(es[p][1], '%d-%m-%Y %H:%M').weekday() == 0:
        firstMondayPosition = p
        break
plt.plot(freq[firstMondayPosition: firstMondayPosition + 30*24], x[firstMondayPosition: firstMondayPosition + 30*24])
plt.savefig("ex1g.pdf", format="pdf", bbox_inches="tight")
plt.show()

import numpy as np

def print_polynomial(p):
    for i in range(len(p)-1):
        print(str(p[i]) + '*x^' + str(i), end=' + ')
    print(str(p[len(p)-1]) + '*x^' + str(len(p)-1))


n = np.random.randint(100)
p = np.random.randint(1000, size=n)
q = np.random.randint(1000, size=n)
r = [0] * 2 * n

print_polynomial(p)
print_polynomial(q)

# inmultire directa
for c1, i1 in enumerate(p):
    for c2, i2 in enumerate(q):
        r[c1 + c2] += i1 * i2

print("Direct multiplication")
print_polynomial(r)

#fft
pfft = np.fft.fft(p)
qfft = np.fft.fft(q)
rfft = abs(pfft) * abs(qfft)

print("FFT multiplication")
print_polynomial(np.fft.ifft(abs(rfft)))

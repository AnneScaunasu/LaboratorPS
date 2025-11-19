import numpy as np


def convolution(p,q):
    r = np.zeros(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            r[i+j] += p[i]*q[j]
    return r


N = 10
p = np.random.rand(np.random.randint(N))
q = np.random.rand(np.random.randint(N))

print(f"Polinomul p initial: {p}")
print(f"Polinomul q initial: {q}")
print(f"Polinomul rezultat prin convolutie: {convolution(p,q)}")

P = np.fft.fft(p,len(p) + len(q) - 1)
Q = np.fft.fft(q,len(p) + len(q) - 1)
Z = P * Q
r = np.fft.ifft(Z)

print(f"Polinomul rezultat prin fft: {r.real}")

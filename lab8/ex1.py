import matplotlib.pyplot as plt
import numpy as np


# a
N = 1000
t = np.arange(0, 1, 1/N)
trend = 15 * (t ** 2) + 30 * t - 12
season = np.cos(2 * np.pi * t * 35) + np.cos(2 * np.pi * t * 53)
noise = np.random.normal(0,1,N)
series_raw = trend + season + noise

fig, ass = plt.subplots(4)

ass[0].plot(t, series_raw)
ass[0].set_title("Seria de timp")

ass[1].plot(t, trend)
ass[1].set_title("Trend")

ass[2].plot(t, season)
ass[2].set_title("Sezon")

ass[3].plot(t, noise)
ass[3].set_title("Variatii")

plt.savefig("ex1a.pdf", format="pdf", bbox_inches="tight")
plt.show()

# b
series = series_raw - np.mean(series_raw)
m = 20
p = 20
gamma = [
    np.sum([series[j]*series[j-t] for j in range(t+m, N)])
    for t in range(p)
]

np_gamma = np.correlate(series, series, mode='full')

fig, ass = plt.subplots(2)

ass[0].plot(gamma)
ass[0].set_title('Vectorul Auto-corelatie')

mid_np = len(np_gamma) // 2
ass[1].plot(np_gamma[mid_np:mid_np + p])
ass[1].set_title('numpy.correlate')

plt.savefig("ex1b.pdf", format="pdf", bbox_inches="tight")
plt.show()

# c
GAMMA = [[gamma[abs(i-j)] for j in range(p)] for i in range(p)]
sol_star = np.dot(np.linalg.inv(GAMMA), gamma)

used_values = series[N-2 * p: N-p]
predicted_values = []

for i in range(p - 1, 2 * p):
    predicted_value = np.dot(sol_star, used_values)
    predicted_values.append(predicted_value)
    used_values = np.append(used_values[1:], predicted_value)

fig, ass = plt.subplots(2)

ass[0].plot(predicted_values)
ass[0].set_title('Valori prezise')

ass[1].plot(series[N-p:])
ass[1].set_title('Valori reale')

plt.savefig("ex1c.pdf", format="pdf", bbox_inches="tight")
plt.show()

# d
min_err = np.inf
min_p_m = (-1,-1)
values = (-1, -1)

for p in range(1,31):
    for m in {0,p}:
        gamma_p = [
            np.sum([series[j] * series[j - t] for j in range(t + m, N)])
            for t in range(p)
        ]
        GAMMA_P = [[gamma_p[abs(i - j)] for j in range(p)] for i in range(p)]
        sol_star = np.dot(np.linalg.inv(GAMMA_P), gamma_p)
        used_values = series[N-2 * p: N-p]
        predicted_value = np.dot(sol_star, used_values)
        mse = (series[N-p] - predicted_value) ** 2
        if mse < min_err:
            min_err = mse
            min_p_m = (p,m)
            values = (series[N-p], predicted_value)

print(f"Cea mai buna performanta de predictie pentru o singura valoare o face modelul AR {min_p_m[0]} si orizontul "
      f"{min_p_m[1]} cu valoarea reala: {values[0]} si cea prezisa {values[1]}")

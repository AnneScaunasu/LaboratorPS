import numpy as np
from generrateSeries import generate_series


def exponential_averaging(initial_series, α):
    s = []
    for i in range(len(initial_series)):
        if i == 0:
            s.append(initial_series[i])
        else:
            s.append(α * initial_series[i] + (1 - α) * s[i - 1])

    return s


def double_exponential_averaging(initial_series, α, β):
    s = []
    b = []
    x = [0] # m = 1 ales aleator m >= 1; initializand x[0]=0 automat fiecare append o sa fie la i + 1 aka i + m
    for i in range(len(initial_series)):
        if i == 0:
            s.append(initial_series[i])
            b.append(initial_series[1] - initial_series[0])
        else:
            s.append(α * initial_series[i] + (1 - α) * (s[i - 1] + b[i - 1]))
            b.append(β * (initial_series[i] - s[i - 1]) + (1 - β) * b[i - 1])
        x.append(s[i] + b[i]) # s[i] + 1 * b[i]

    return x[1:]


def triple_exponential_averaging(initial_series, α, β, γ, L):
    s = []
    b = []
    c = []
    x = [0] # m = 1 ales aleator m >= 1; initializand x[0]=0 automat fiecare append o sa fie la i + 1 aka i + m

    for i in range(len(initial_series)):
        if i == 0:
            s.append(initial_series[i])
            b.append(initial_series[1] - initial_series[0])
            x.append(s[i] + b[i])
        elif i < L:
            s.append(α * initial_series[i] + (1 - α) * (s[i - 1] + b[i - 1]))
            b.append(β * (initial_series[i] - s[i - 1]) + (1 - β) * b[i - 1])
            c.append(initial_series[i] - np.mean(initial_series[:L]))
            x.append(s[i] + b[i])
        else:
            s.append(α * (initial_series[i] - c[i - L]) + (1 - α) * (s[i - 1] + b[i - 1]))
            b.append(β * (s[i] - s[i - 1]) + (1 - β) * b[i - 1])
            c.append(γ * (initial_series[i] - s[i] - b[i - 1]) + (1 - γ) * c[i - L])
            x.append(s[i] + b[i] + c[(i - L + 1) % L])

    return x[1:]


trend, season, noise = generate_series()
series = trend + season + noise

# normal
min_error = np.inf
best_α = -1
α_set = [i/20 for i in range(21)]
for α in α_set:
    resulted_series = exponential_averaging(series, α)
    mse = np.average((series - resulted_series) ** 2)
    if mse < min_error:
        min_error = mse
        best_α = α
print(f"Cea mai buna performanta a medierii exponentiale normale a fost atinsa pentru α={best_α} cu eroarea {min_error}")

#  double
min_error = np.inf
best_α_β = (-1,-1)
α_set = [i/20 for i in range(21)]
β_set = [i/20 for i in range(21)]
for α in α_set:
    for β in β_set:
        resulted_series = double_exponential_averaging(series, α, β)
        mse = np.average((series - resulted_series) ** 2)
        if mse < min_error:
            min_error = mse
            best_α_β = (α,β)
print(f"Cea mai buna performanta a medierii exponentiale duble a fost atinsa pentru α={best_α_β[0]} si β={best_α_β[1]} cu eroarea {min_error}")

# triple
x_season = season - np.mean(season)
fft = np.abs(np.fft.rfft(x_season))
freqs = np.fft.rfftfreq(len(season), d=1)
fft[0] = 0
L = (np.argsort(fft)[-2:])[0]

min_error = np.inf
best_α_β_γ = (-1,-1,-1)
α_set = [i/20 for i in range(21)]
β_set = [i/20 for i in range(21)]
γ_set = [i/20 for i in range(21)]
for α in α_set:
    for β in β_set:
        for γ in γ_set:
            resulted_series = triple_exponential_averaging(series, α, β, γ, L)
            mse = np.average((series - resulted_series) ** 2)
            if mse < min_error:
                min_error = mse
                best_α_β_γ = (α,β,γ)
print(f"Cea mai buna performanta a medierii exponentiale triple a fost atinsa pentru α={best_α_β_γ[0]}, β={best_α_β_γ[1]} si γ={best_α_β_γ[2]} cu eroarea {min_error}")

import numpy as np
import matplotlib.pylab as plt
from generate_series import generate_series


# 3
def ar_model_with_regressors(series, m, p, regressors):
    N = len(series)
    sorted_regressors = sorted(regressors)
    gamma = [
        np.sum([series[j] * series[j - t] for j in range(N - p - m, N - p + 1)])
        for t in range(p+1)
    ]

    GAMMA = [[gamma[abs(si - sj)] for sj in sorted_regressors] for si in sorted_regressors]
    sol_star = np.dot(np.linalg.inv(GAMMA), np.array([gamma[i] for i in sorted_regressors]))
    sol_star_reduced = np.zeros(p)
    for coeff, regressor in zip(sol_star, sorted_regressors):
        sol_star_reduced[regressor-1] = coeff

    predicted_values = []

    for i in range(N-p, N):
        predicted_value = np.sum([sol_star_reduced[regressor-1] * series[i - regressor] for regressor in sorted_regressors])
        predicted_values.append(predicted_value)
    return (np.mean(np.pow(predicted_values - series[N-p:],2)), predicted_values)


def ar_model_greedy(series, m, p):
    min_error = np.inf
    selected_regressors = []
    remaining_regressors = list(range(1, p+1))
    previous_error = np.inf
    best_predicted_values = []
    ε = 1

    while True:
        best_error = previous_error
        best_regressor = None
        for regressor in remaining_regressors:
            loop_regressors = selected_regressors + [regressor]
            error_loop, predicted_values = ar_model_with_regressors(series, p, m, loop_regressors)

            if error_loop < best_error:
                best_error = error_loop
                best_regressor = regressor
                best_predicted_values = predicted_values
        if best_regressor is None:
            break
        if previous_error - best_error < ε:
            break
        selected_regressors.append(best_regressor)
        remaining_regressors.remove(best_regressor)
        previous_error = best_error
    return best_predicted_values


# 4
def solutie_polinom(params):
    n = len(params)
    C = np.zeros((n,n))
    for i in range(n):
        if i != 0:
            C[i][i-1] = 1
        C[i][n-1] = -params[i]
    print(C)
    return np.linalg.eig(C).eigenvalues


# testarea rezolvarilor
def rezolvarea_polinomului(params, solutie):
    rezolvare = 0
    for i in range(len(params)):
        rezolvare += np.pow(solutie, i) * params[i]
    return rezolvare


# 1
N = 1000
trend, season, noise = generate_series(N)
series = trend + noise + season

# 2
p = 20
m = 20
gamma = [
    np.sum([series[j]*series[j-t] for j in range((N-p-1)-m, N-p)])
    for t in range(1,p+1)
]

GAMMA = [[gamma[abs(i-j)] for j in range(p)] for i in range(p)]
sol_star = np.dot(np.linalg.inv(GAMMA), gamma)

used_values = series[N - (2 * p): N-p]
predicted_values = []

for _ in range(p - 1, 2 * p):
    predicted_value = np.dot(np.transpose(sol_star), np.transpose(used_values))
    predicted_values.append(predicted_value)
    used_values = np.append(used_values[1:], predicted_value)

fig, ass = plt.subplots(2)

ass[0].plot(predicted_values)
ass[0].set_title('Valori prezise')

ass[1].plot(series[N-p:])
ass[1].set_title('Valori reale')

plt.savefig("ex2.pdf", format="pdf", bbox_inches="tight")
plt.show()

# 3
# a
greedy_prediction = ar_model_greedy(series, m, p)
fig, ass = plt.subplots(2)

ass[0].plot(greedy_prediction)
ass[0].set_title('Valori prezise greedy')

ass[1].plot(series[N-p:])
ass[1].set_title('Valori reale')

plt.savefig("ex3a.pdf", format="pdf", bbox_inches="tight")
plt.show()

# b

# 4
params_polinom = [-1/3, 5/3]
solutii = solutie_polinom(params_polinom)
print(f"Pentru polinomul p(L) = 1 − 5L − 3L^2, avem solutiile: {solutii}")
print(f"Rezolvarile pentru solutiile anterioare sunt:\n"
      f" -> {solutii[0].real} => {rezolvarea_polinomului(params_polinom, solutii[0])}\n"
      f" -> {solutii[1].real} => {rezolvarea_polinomului(params_polinom, solutii[1])}\n")

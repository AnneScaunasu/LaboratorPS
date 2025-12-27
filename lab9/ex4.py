import warnings

import numpy as np
from statsmodels.tools.sm_exceptions import ConvergenceWarning
from statsmodels.tsa.arima.model import ARIMA

from ex2 import series

p_values = [i for i in range(1, 21)]
q_values = [i for i in range(1, 21)]
d = 2 # luat aleator pentru un trend care se schimba in timp
series_c = series - series.mean()

min_bic = np.inf
min_vals = (-1,-1)

for p in p_values:
    for q in q_values:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", ConvergenceWarning)
                warnings.simplefilter("ignore", UserWarning)
                model = ARIMA(series_c, order=(p, d, q))
                model_fit = model.fit()
                print(f"Model finalizat pentru p={p}, q={q}") # pentru a putea urmarii progresul

            if not model_fit.mle_retvals.get("converged", True):
                continue

            # folosim bic (bayesian information criterion) pentru a gasii cele mai bune p si q pentru un model ARMA
            # bic = -2logL + klogN
            # L - calitatea fit-ului (cat de bine explica datele)
            # k - numarul de parametrii (cat de complex este)
            # N - numarul de observatii

            # Initial am vrut sa folosesc mse, dar acesta nu penaliza cat de complex devenea modelul
            # Exemplu de rezultat cu mse: Cea mai buna performata a modelului ARIMA a fost pentru p= 15, d=0 si q=17 cu eroarea 3.5899439461551337
            if model_fit.bic < min_bic:
                min_bic = model_fit.bic
                min_vals = (p, q)
        except Exception:
            continue

print(f"Cea mai buna performata a modelului ARIMA a fost pentru p={min_vals[0]}, d=2 si q={min_vals[1]} cu criteriul BIC {min_bic}")
# Cea mai buna performata a modelului ARIMA a fost pentru p=15, d=0 si q=17 cu eroarea 3.5899439461551337
# Cea mai buna performata a modelului ARIMA a fost pentru p=1, d=2 si q=2 cu criteriul BIC 3160.7582011177515

import numpy as np
import matplotlib.pyplot as plt
from ex2 import series

q = 20
θ = np.full(q, 1/2) #arbitrar
mean = np.mean(series)
predicted_series = []
last_error = np.zeros(q)

for value in series:
    predicted_value = mean + np.sum(last_error * θ)
    predicted_series.append(predicted_value)
    last_error = np.append(last_error[1:], (value - predicted_value))

_, ass = plt.subplots(2)

ass[0].plot(series)
ass[0].set_title('original series')

ass[1].plot(predicted_series)
ass[1].set_title('MA model')

plt.savefig("ex3.pdf", format="pdf", bbox_inches="tight")
plt.show()

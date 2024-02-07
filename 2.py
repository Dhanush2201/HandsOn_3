import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

n_values = np.arange(1, 1001, 10)
execution_times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, 'o', label='Measured Time')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Execution Time vs. Input Size')
plt.grid(True)

def polynomial_fit(x, a, b, c):
    return a * x**2 + b * x + c

popt, pcov = curve_fit(polynomial_fit, n_values, execution_times)
fitted_curve = polynomial_fit(n_values, *popt)
plt.plot(n_values, fitted_curve, label='Polynomial Fit', color='red')

plt.legend()
plt.show()

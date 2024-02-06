#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

# Timing the function for various values of n
n_values = np.arange(1, 1001)  # Adjust the range as needed
runtimes = []

for n in n_values:
    time_result = get_ipython().run_line_magic('timeit', '-n 1 -r 1 -o f(n)')
    runtimes.append(time_result.average)

# Plotting time vs n
plt.figure(figsize=(10, 6))
plt.plot(n_values, runtimes, 'b.', label='Data')

# Fitting a polynomial curve to the data
def polynomial_curve(x, a, b, c):
    return a * x**2 + b * x + c

popt, _ = curve_fit(polynomial_curve, n_values, runtimes)
fitted_curve = polynomial_curve(n_values, *popt)
plt.plot(n_values, fitted_curve, 'r-', label='Fitted Curve')

# Determining upper and lower bounds (polynomials) on the curve
upper_bound = fitted_curve + 0.1  # Adjust as needed
lower_bound = fitted_curve - 0.1  # Adjust as needed
plt.plot(n_values, upper_bound, 'g--', label='Upper Bound')
plt.plot(n_values, lower_bound, 'm--', label='Lower Bound')

plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time vs n for Function f')
plt.legend()
plt.show()


# In[ ]:





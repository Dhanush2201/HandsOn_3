#3
a, b, c = popt

# Define upper and lower bound polynomials
def upper_bound(x):
    return a * x**2 + b * x + c

def lower_bound(x):
    return np.full_like(x, execution_times[0])  # Constant value matching the first execution time

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, 'o', label='Measured Time')
plt.plot(n_values, upper_bound(n_values), label='Upper Bound (Quadratic)', color='red')
plt.plot(n_values, lower_bound(n_values), label='Lower Bound (Constant)', color='green')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Execution Time vs. Input Size with Upper and Lower Bounds')
plt.grid(True)
plt.legend()
plt.show()

#4

plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, 'o', label='Measured Time')
plt.plot(n_values, upper_bound(n_values), label='Upper Bound (Quadratic)', color='red')
plt.plot(n_values, lower_bound(n_values), label='Lower Bound (Constant)', color='green')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Execution Time vs. Input Size with Upper and Lower Bounds')
plt.grid(True)
plt.legend()

plt.xlim(0, 50)  
plt.ylim(0, 0.5)  

n_0 = 10 
plt.axvline(x=n_0, color='black', linestyle='--', label=f'$n_0 = {n_0}$')
plt.legend()

plt.show()
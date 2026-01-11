import numpy as np

def monte_carlo_pi(num_samples=1000000):
    # Generate random points (x, y) in the range [0, 1]
    x = np.random.uniform(0, 1, num_samples)
    y = np.random.uniform(0, 1, num_samples)
    
    # Count points inside the quarter-circle
    inside_circle = np.sum(x**2 + y**2 <= 1)
    
    # Estimate Pi
    pi_estimate = 4 * (inside_circle / num_samples)
    return pi_estimate

# Run the simulation
estimated_pi = monte_carlo_pi(100000000)
print(f"Estimated π: {estimated_pi}")

import random
import scipy.integrate as spi


def monte_carlo_integration(func, a, b, num_samples):
    total = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += func(x)

    return (b - a) * (total / num_samples)


def f(x):
    return x**2


a = 0
b = 2
num_samples = 1000000

result = monte_carlo_integration(f, a, b, num_samples)

print("Approximate Integral Value:", result)

result, error = spi.quad(f, a, b)

print("Інтеграл: ", result)

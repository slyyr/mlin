import numpy as np
from scipy import stats

sample = [172, 174, 168, 169, 171, 173, 175, 170, 169, 172]

population_mean = 170
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
n = len(sample)

# t-test

t_stats = (sample_mean - population_mean) / (sample_std / np.sqrt(n))

p_value = 2 * (1 - stats.t.cdf(abs(t_stats), df = n - 1))

alpha = 0.05

if p_value < alpha:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
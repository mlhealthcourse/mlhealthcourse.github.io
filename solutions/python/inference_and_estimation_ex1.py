import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)
n_sims = 100
n_per_group = 50
true_diff = 5
sd_val = 10

contains_true = []
lower_bounds = []
upper_bounds = []

for i in range(n_sims):
    group1 = np.random.normal(0, sd_val, n_per_group)
    group2 = np.random.normal(true_diff, sd_val, n_per_group)

    diff = np.mean(group2) - np.mean(group1)
    se = np.sqrt(np.var(group1, ddof=1)/n_per_group + np.var(group2, ddof=1)/n_per_group)
    t_crit = stats.t.ppf(0.975, df=n_per_group*2 - 2)

    lower = diff - t_crit * se
    upper = diff + t_crit * se

    lower_bounds.append(lower)
    upper_bounds.append(upper)
    contains_true.append(lower <= true_diff <= upper)

print(f"Proportion of CIs containing true value: {np.mean(contains_true):.2f}")

# Visualize
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(n_sims):
    color = "green" if contains_true[i] else "red"
    ax.plot([i, i], [lower_bounds[i], upper_bounds[i]], color=color, linewidth=0.8)

ax.axhline(y=true_diff, color="blue", linestyle="--", label="True difference")
ax.set_xlabel("Simulation")
ax.set_ylabel("Mean Difference")
ax.set_title("95% Confidence Intervals from 100 Simulated Trials")
ax.legend()
plt.tight_layout()
plt.show()
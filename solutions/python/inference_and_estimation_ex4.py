from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()

# Cohen's d = delta / sd = 0.4 / 1.2
effect_size = 0.4 / 1.2

# 80% power
n_80 = analysis.solve_power(effect_size=effect_size, alpha=0.05, power=0.80,
                            alternative='two-sided')
print(f"Sample size per group (80% power): {int(np.ceil(n_80))}")

# 90% power
n_90 = analysis.solve_power(effect_size=effect_size, alpha=0.05, power=0.90,
                            alternative='two-sided')
print(f"Sample size per group (90% power): {int(np.ceil(n_90))}")

print(f"\nIncreasing from 80% to 90% power requires about "
      f"{int(round((n_90/n_80 - 1) * 100))}% more participants per group.")
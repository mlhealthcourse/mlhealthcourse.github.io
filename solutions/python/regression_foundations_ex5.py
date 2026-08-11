
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

np.random.seed(42)
n = 300
age = np.random.uniform(30, 75, n).round()
sex = np.random.binomial(1, 0.5, n)  # 1 = male

# True interaction: steeper age slope for males
sbp = 80 + 0.45 * age + (-8 + 0.25 * age) * sex + np.random.normal(0, 10, n)

df = pd.DataFrame({'age': age, 'sex': sex, 'sbp': sbp})

# Model WITHOUT interaction
model_no_int = smf.ols('sbp ~ age + C(sex)', data=df).fit()
print("=== Model without interaction ===")
print(model_no_int.summary())

# Model WITH interaction
model_int = smf.ols('sbp ~ age * C(sex)', data=df).fit()
print("\n=== Model with interaction ===")
print(model_int.summary())

# Compare models (likelihood ratio test)
from scipy.stats import chi2
lr_stat = -2 * (model_no_int.llf - model_int.llf)
lr_p = chi2.sf(lr_stat, df=1)
print(f"\nLikelihood ratio test: chi2={lr_stat:.2f}, p={lr_p:.4f}")

# Visualization
fig, ax = plt.subplots(figsize=(8, 6))
for s, label, color in [(0, 'Female', 'coral'), (1, 'Male', 'steelblue')]:
    mask = df['sex'] == s
    ax.scatter(df.loc[mask, 'age'], df.loc[mask, 'sbp'],
               alpha=0.3, color=color, label=label)
    age_range = np.linspace(30, 75, 100)
    pred = model_int.params['Intercept'] + model_int.params['age'] * age_range
    if s == 1:
        pred += model_int.params['C(sex)[T.1]'] + model_int.params['age:C(sex)[T.1]'] * age_range
    ax.plot(age_range, pred, color=color, linewidth=2)

ax.set_xlabel('Age (years)')
ax.set_ylabel('Systolic Blood Pressure (mmHg)')
ax.set_title('Age-SBP Relationship by Sex')
ax.legend()
plt.tight_layout()
plt.show()

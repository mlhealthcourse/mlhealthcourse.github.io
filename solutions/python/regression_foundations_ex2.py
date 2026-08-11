
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

np.random.seed(42)
n = 150
age = np.random.uniform(30, 75, n).round()
sex = np.random.binomial(1, 0.5, n)
# BMI increases slightly with age (confounding)
bmi = 22 + 0.08 * age + 2 * sex + np.random.normal(0, 3, n)
# SBP depends on age, sex, AND BMI
sbp = 70 + 0.45 * age + 4 * sex + 1.0 * bmi + np.random.normal(0, 10, n)

df = pd.DataFrame({'age': age, 'sex': sex, 'bmi': bmi, 'sbp': sbp})

# Unadjusted model
model_unadj = smf.ols('sbp ~ age', data=df).fit()
print("=== Unadjusted Model ===")
print(f"Age coefficient: {model_unadj.params['age']:.3f}")
print(f"R-squared: {model_unadj.rsquared:.3f}\n")

# Adjusted model
model_adj = smf.ols('sbp ~ age + C(sex) + bmi', data=df).fit()
print("=== Adjusted Model ===")
print(model_adj.summary())
print(f"\nAge coefficient (unadjusted): {model_unadj.params['age']:.3f}")
print(f"Age coefficient (adjusted): {model_adj.params['age']:.3f}")
print(f"Change: {model_unadj.params['age'] - model_adj.params['age']:.3f}")

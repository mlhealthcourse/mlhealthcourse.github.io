
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.special import expit

np.random.seed(42)
n = 500

age = np.random.uniform(35, 75, n).round()
male = np.random.binomial(1, 0.5, n)
smoker = np.random.binomial(1, 0.25, n)
cholesterol = np.random.normal(220, 40, n).round()

# Generate CHD outcome
log_odds = -7 + 0.06 * age + 0.5 * male + 0.4 * smoker + 0.008 * cholesterol
prob_chd = expit(log_odds)
chd = np.random.binomial(1, prob_chd)

df = pd.DataFrame({
    'age': age, 'male': male, 'smoker': smoker,
    'cholesterol': cholesterol, 'chd': chd
})

print(f"CHD prevalence: {chd.mean():.3f}\n")

# Fit logistic regression
model = smf.logit('chd ~ age + male + smoker + cholesterol', data=df).fit()
print(model.summary())

# Odds ratios with 95% CI
params = model.params[1:]  # exclude intercept
conf = model.conf_int().iloc[1:]
or_table = pd.DataFrame({
    'OR': np.exp(params),
    'Lower 95% CI': np.exp(conf[0]),
    'Upper 95% CI': np.exp(conf[1])
})
print("\nOdds Ratios:")
print(or_table.round(3))

# Predicted probability for a specific patient
new_patient = pd.DataFrame({
    'age': [60], 'male': [1], 'smoker': [1], 'cholesterol': [260]
})
pred_prob = model.predict(new_patient)
print(f"\nPredicted CHD probability for 60yo male smoker, chol=260: {pred_prob.values[0]:.3f}")


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

np.random.seed(42)
n = 150
age = np.random.uniform(30, 75, n).round()
sbp = 85 + 0.6 * age + np.random.normal(0, 12, n)

clinical_data = pd.DataFrame({'age': age, 'sbp': sbp})

# Fit the model
X = sm.add_constant(clinical_data['age'])
model = sm.OLS(clinical_data['sbp'], X).fit()
print(model.summary())

print(f"\nIntercept: {model.params['const']:.2f} mmHg")
print(f"Slope: {model.params['age']:.3f} mmHg per year of age")
print(f"R-squared: {model.rsquared:.3f}")
print(f"95% CI for slope: ({model.conf_int().loc['age', 0]:.3f}, "
      f"{model.conf_int().loc['age', 1]:.3f})")

# Scatterplot with regression line
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(age, sbp, alpha=0.5)
age_range = np.linspace(30, 75, 100)
predicted = model.params['const'] + model.params['age'] * age_range
ax.plot(age_range, predicted, 'b-', linewidth=2, label='Regression line')
ax.set_xlabel('Age (years)')
ax.set_ylabel('Systolic Blood Pressure (mmHg)')
ax.set_title('Age vs. Systolic Blood Pressure')
ax.legend()
plt.tight_layout()
plt.show()

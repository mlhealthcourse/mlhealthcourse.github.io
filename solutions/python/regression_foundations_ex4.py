
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n = 150
age = np.random.uniform(30, 75, n).round()
sbp = 85 + 0.6 * age + np.random.normal(0, 12, n)
df = pd.DataFrame({'age': age, 'sbp': sbp})

model = smf.ols('sbp ~ age', data=df).fit()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residuals vs Fitted
axes[0, 0].scatter(model.fittedvalues, model.resid, alpha=0.5)
axes[0, 0].axhline(y=0, color='red', linestyle='--')
axes[0, 0].set_xlabel('Fitted Values')
axes[0, 0].set_ylabel('Residuals')
axes[0, 0].set_title('Residuals vs Fitted')

# 2. Q-Q Plot
stats.probplot(model.resid, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Normal Q-Q Plot')

# 3. Scale-Location
std_resid = np.sqrt(np.abs(model.get_influence().resid_studentized_internal))
axes[1, 0].scatter(model.fittedvalues, std_resid, alpha=0.5)
axes[1, 0].set_xlabel('Fitted Values')
axes[1, 0].set_ylabel('sqrt(|Standardized Residuals|)')
axes[1, 0].set_title('Scale-Location')

# 4. Residuals vs Leverage
sm.graphics.influence_plot(model, ax=axes[1, 1], criterion="cooks")
axes[1, 1].set_title('Residuals vs Leverage')

plt.tight_layout()
plt.show()

# Formal test for normality
shapiro_stat, shapiro_p = stats.shapiro(model.resid)
print(f"Shapiro-Wilk test for normality: W={shapiro_stat:.4f}, p={shapiro_p:.4f}")

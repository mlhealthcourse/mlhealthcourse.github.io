import numpy as np
from statsmodels.stats.multitest import multipletests

np.random.seed(123)
n_genes = 1000
n_true = 50

# Null p-values (uniform) and true effect p-values (small)
p_null = np.random.uniform(0, 1, n_genes - n_true)
p_true = np.random.beta(1, 20, n_true)

p_values = np.concatenate([p_null, p_true])

print(f"Nominally significant (p < 0.05): {np.sum(p_values < 0.05)}")

# Bonferroni correction
reject_bonf, pvals_bonf, _, _ = multipletests(p_values, alpha=0.05, method='bonferroni')
print(f"Significant after Bonferroni: {np.sum(reject_bonf)}")

# BH-FDR correction
reject_fdr, pvals_fdr, _, _ = multipletests(p_values, alpha=0.05, method='fdr_bh')
print(f"Significant after BH-FDR: {np.sum(reject_fdr)}")

print("\nBonferroni is much more conservative.")
print("FDR retains more discoveries while controlling the false discovery rate.")
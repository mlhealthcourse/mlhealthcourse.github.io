# Simulate 1000 p-values: 950 null (uniform), 50 truly differentially expressed
set.seed(123)
n_genes <- 1000
n_true <- 50

# Null p-values are uniformly distributed
p_null <- runif(n_genes - n_true, 0, 1)

# True effects: p-values will tend to be small
p_true <- rbeta(n_true, 1, 20) # skewed toward 0

p_values <- c(p_null, p_true)

# How many nominally significant?
cat("Nominally significant (p < 0.05):", sum(p_values < 0.05), "\n")

# Bonferroni correction
p_bonferroni <- p.adjust(p_values, method = "bonferroni")
cat("Significant after Bonferroni:", sum(p_bonferroni < 0.05), "\n")

# BH-FDR correction
p_fdr <- p.adjust(p_values, method = "BH")
cat("Significant after BH-FDR:", sum(p_fdr < 0.05), "\n")

# Compare
cat("\nBonferroni is much more conservative.\n")
cat(
  "FDR retains more discoveries while controlling the false discovery rate.\n"
)
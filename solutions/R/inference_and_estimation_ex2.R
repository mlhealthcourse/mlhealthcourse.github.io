# This is a conceptual exercise, but let's verify the numbers:
p_control <- 0.12
p_treatment <- 0.09

risk_difference <- p_control - p_treatment
risk_ratio <- p_treatment / p_control
nnt <- 1 / risk_difference

cat("Risk Difference:", round(risk_difference, 3), "\n")
cat("Risk Ratio:", round(risk_ratio, 3), "\n")
cat("NNT:", round(nnt, 1), "\n")

set.seed(42)
n <- 150
age <- round(runif(n, 30, 75))
sex <- rbinom(n, 1, 0.5) # 1 = male
# BMI increases slightly with age (confounding)
bmi <- 22 + 0.08 * age + 2 * sex + rnorm(n, 0, 3)
# SBP depends on age, sex, AND BMI
sbp <- 70 + 0.45 * age + 4 * sex + 1.0 * bmi + rnorm(n, 0, 10)

df <- data.frame(
  age = age,
  sex = factor(sex, labels = c("Female", "Male")),
  bmi = bmi,
  sbp = sbp
)

# Unadjusted model (age only)
model_unadj <- lm(sbp ~ age, data = df)
cat("=== Unadjusted Model ===\n")
cat("Age coefficient:", round(coef(model_unadj)["age"], 3), "\n")
cat("R-squared:", round(summary(model_unadj)$r.squared, 3), "\n\n")

# Adjusted model (age + sex + BMI)
model_adj <- lm(sbp ~ age + sex + bmi, data = df)
cat("=== Adjusted Model ===\n")
summary(model_adj)
cat("\nAge coefficient (unadjusted):", round(coef(model_unadj)["age"], 3), "\n")
cat("Age coefficient (adjusted):", round(coef(model_adj)["age"], 3), "\n")
cat(
  "Change:",
  round(coef(model_unadj)["age"] - coef(model_adj)["age"], 3),
  "\n"
)


set.seed(42)
n <- 500

age <- round(runif(n, 35, 75))
male <- rbinom(n, 1, 0.5)
smoker <- rbinom(n, 1, 0.25)
cholesterol <- round(rnorm(n, 220, 40))

# Generate CHD outcome (binary) based on logistic model
log_odds <- -7 + 0.06 * age + 0.5 * male + 0.4 * smoker + 0.008 * cholesterol
prob_chd <- plogis(log_odds) # inverse logit
chd <- rbinom(n, 1, prob_chd)

df <- data.frame(
  age,
  male = factor(male),
  smoker = factor(smoker),
  cholesterol,
  chd
)

cat("CHD prevalence:", round(mean(chd), 3), "\n\n")

# Fit logistic regression
model <- glm(
  chd ~ age + male + smoker + cholesterol,
  data = df,
  family = binomial
)
summary(model)

# Odds ratios with 95% CI
or_table <- data.frame(
  OR = exp(coef(model)),
  Lower = exp(confint(model))[, 1],
  Upper = exp(confint(model))[, 2]
)
cat("\nOdds Ratios:\n")
print(round(or_table[-1, ], 3)) # Exclude intercept

# Predicted probability for a specific patient
new_patient <- data.frame(
  age = 60,
  male = factor(1),
  smoker = factor(1),
  cholesterol = 260
)
pred_prob <- predict(model, newdata = new_patient, type = "response")
cat(
  "\nPredicted CHD probability for 60-year-old male smoker with",
  "cholesterol 260:",
  round(pred_prob, 3),
  "\n"
)

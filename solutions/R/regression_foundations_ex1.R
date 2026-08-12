
# Simulate clinical data
set.seed(42)
n <- 150
age <- round(runif(n, 30, 75))
sbp <- 85 + 0.6 * age + rnorm(n, 0, 12)

clinical_data <- data.frame(age = age, sbp = sbp)

# Fit the model
model <- lm(sbp ~ age, data = clinical_data)
summary(model)

# Interpret
cat("\nIntercept:", round(coef(model)[1], 3), "mmHg\n")
cat("Slope:", round(coef(model)[2], 3), "mmHg per year of age\n")
cat("R-squared:", round(summary(model)$r.squared, 3), "\n")

# Confidence interval for the slope
confint(model, "age", level = 0.95)

# Scatterplot with regression line
library(ggplot2)
ggplot(clinical_data, aes(x = age, y = sbp)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = TRUE, color = "blue") +
  labs(
    x = "Age (years)",
    y = "Systolic Blood Pressure (mmHg)",
    title = "Age vs. Systolic Blood Pressure"
  ) +
  theme_minimal()

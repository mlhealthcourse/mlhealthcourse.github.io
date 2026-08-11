
set.seed(42)
n <- 300
age <- round(runif(n, 30, 75))
sex <- factor(rbinom(n, 1, 0.5), labels = c("Female", "Male"))

# True interaction: steeper age slope for males
sbp <- 80 +
  0.45 * age +
  ifelse(sex == "Male", -8 + 0.25 * age, 0) +
  rnorm(n, 0, 10)

df <- data.frame(age = age, sex = sex, sbp = sbp)

# Model WITHOUT interaction
model_no_int <- lm(sbp ~ age + sex, data = df)
cat("=== Model without interaction ===\n")
summary(model_no_int)

# Model WITH interaction
model_int <- lm(sbp ~ age * sex, data = df)
cat("\n=== Model with interaction ===\n")
summary(model_int)

# Is the interaction significant?
anova(model_no_int, model_int)

# Visualization
library(ggplot2)
ggplot(df, aes(x = age, y = sbp, color = sex)) +
  geom_point(alpha = 0.3) +
  geom_smooth(method = "lm", se = TRUE) +
  labs(
    x = "Age (years)",
    y = "Systolic Blood Pressure (mmHg)",
    title = "Age-SBP Relationship by Sex",
    subtitle = "Steeper slope for males indicates an interaction"
  ) +
  theme_minimal() +
  scale_color_manual(values = c("Female" = "coral", "Male" = "steelblue"))

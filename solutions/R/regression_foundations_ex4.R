
set.seed(42)
n <- 150
age <- round(runif(n, 30, 75))
sbp <- 85 + 0.6 * age + rnorm(n, 0, 12)
df <- data.frame(age = age, sbp = sbp)

model <- lm(sbp ~ age, data = df)

# Standard diagnostic plots (2x2)
par(mfrow = c(2, 2))
plot(model)
par(mfrow = c(1, 1))

# Or using ggplot2 for prettier diagnostics
library(ggplot2)
library(patchwork)

diag_data <- data.frame(
  fitted = fitted(model),
  residuals = resid(model),
  std_residuals = rstandard(model)
)

p1 <- ggplot(diag_data, aes(x = fitted, y = residuals)) +
  geom_point(alpha = 0.5) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "red") +
  geom_smooth(se = FALSE, color = "blue") +
  labs(title = "Residuals vs Fitted", x = "Fitted Values", y = "Residuals") +
  theme_minimal()

p2 <- ggplot(diag_data, aes(sample = std_residuals)) +
  stat_qq() +
  stat_qq_line(color = "red") +
  labs(
    title = "Normal Q-Q Plot",
    x = "Theoretical Quantiles",
    y = "Standardized Residuals"
  ) +
  theme_minimal()

p1 + p2

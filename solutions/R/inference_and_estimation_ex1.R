set.seed(42)
n_sims <- 100
n_per_group <- 50
true_diff <- 5
sd_val <- 10

contains_true <- numeric(n_sims)

for (i in 1:n_sims) {
  group1 <- rnorm(n_per_group, mean = 0, sd = sd_val)
  group2 <- rnorm(n_per_group, mean = true_diff, sd = sd_val)

  test_result <- t.test(group2, group1)
  ci <- test_result$conf.int

  contains_true[i] <- (ci[1] <= true_diff & ci[2] >= true_diff)
}

cat(
  "Proportion of CIs containing true value:",
  round(mean(contains_true), 3),
  "\n"
)

# Bonus: visualize the CIs
library(ggplot2)
ci_data <- data.frame(
  sim = 1:n_sims,
  lower = numeric(n_sims),
  upper = numeric(n_sims),
  contains = logical(n_sims)
)

set.seed(42)
for (i in 1:n_sims) {
  group1 <- rnorm(n_per_group, mean = 0, sd = sd_val)
  group2 <- rnorm(n_per_group, mean = true_diff, sd = sd_val)
  test_result <- t.test(group2, group1)
  ci_data$lower[i] <- test_result$conf.int[1]
  ci_data$upper[i] <- test_result$conf.int[2]
  ci_data$contains[i] <- (ci_data$lower[i] <= true_diff &
    ci_data$upper[i] >= true_diff)
}

ggplot(ci_data, aes(x = sim, y = (lower + upper) / 2, color = contains)) +
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.3) +
  geom_hline(yintercept = true_diff, linetype = "dashed", color = "blue") +
  scale_color_manual(values = c("red", "darkgreen")) +
  labs(
    x = "Simulation",
    y = "Mean Difference",
    title = "95% Confidence Intervals from 100 Simulated Trials"
  ) +
  theme_minimal()
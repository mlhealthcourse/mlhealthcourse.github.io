# Using the power.t.test function
# 80% power
result_80 <- power.t.test(
  delta = 0.4, # expected difference
  sd = 1.2, # standard deviation
  sig.level = 0.05,
  power = 0.80,
  type = "two.sample",
  alternative = "two.sided"
)
cat("Sample size per group (80% power):", ceiling(result_80$n), "\n")

# 90% power
result_90 <- power.t.test(
  delta = 0.4,
  sd = 1.2,
  sig.level = 0.05,
  power = 0.90,
  type = "two.sample",
  alternative = "two.sided"
)
cat("Sample size per group (90% power):", ceiling(result_90$n), "\n")

cat(
  "\nIncreasing power from 80% to 90% requires about",
  round((ceiling(result_90$n) / ceiling(result_80$n) - 1) * 100),
  "% more participants per group.\n"
)
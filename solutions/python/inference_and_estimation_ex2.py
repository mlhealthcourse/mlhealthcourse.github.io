# This is a conceptual exercise, but let's verify the numbers:
p_control = 0.12
p_treatment = 0.09

risk_difference = p_control - p_treatment
risk_ratio = p_treatment / p_control
nnt = 1 / risk_difference

print(f"Risk Difference: {risk_difference}")
print(f"Risk Ratio: {risk_ratio:.3f}")
print(f"NNT: {nnt:.1f}")
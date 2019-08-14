def calculate_years(principal, interest, tax, desired, years=0):
    if principal > desired:
        return years
    else:
        growth_pretax = principal * (1+interest)
        taxed_value = (growth_pretax - principal) * tax
        growth_posttax = growth_pretax - taxed_value
        principal = growth_posttax
        return calculate_years(principal, interest, tax, desired, years + 1)

print(calculate_years(1000, 0.05, 0.18, 1100))
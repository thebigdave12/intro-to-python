user_age_input = input("What is your age in years: ")

age_years = int(user_age_input)

age_months = age_years * 12

age_seconds = ((age_years * 12) * 365 * 24 * 60 * 60)

print(f"Your age is {age_months} in months and {age_seconds}")
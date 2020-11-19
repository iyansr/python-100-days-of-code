#  Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age ? ")
int_age = int(age)
days = 365
weeks = 52
months = 12


remaining_day = (90 - int_age) * days
remaining_week = (90 - int_age) * weeks
remaining_month = (90 - int_age) * months


print(
    f"You have {remaining_day} days, {remaining_week} weeks, and {remaining_month} months left.")


# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

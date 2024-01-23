# Write a program that displays a logical error (be as creative as possible!).

print("Welcome to the logical error program!")
print("")

daily_expense = input(str("What is the average cost of your meals per day? "))
weekly_expense = daily_expense * 7
monthly_expense = weekly_expense * 4

print(f"For your food, you spend an average of {weekly_expense} £ every week.")
print(f"A total of {monthly_expense} £ every month.")

monthly_expense = int(monthly_expense)

if monthly_expense > 1000:
    print("\nAre you eating oysters every day?")
else:
    print("\nGreat money managment!")
month_name = input("Enter the month name: ")

if month_name == "Fabruary":
    print(f"No of days in {month_name} is 28 or 29")
elif month_name in ("April", "June", "September", "November"):
    print(f"No of days in {month_name} is 30 days.")
elif month_name in ("January", "March", "May", "July", "August", "October"):
    print(f"No of days in {month_name} is 31 days")
else:
    print("This is invalid input")

import calendar as cal
# Display the calendar for a specific month and year
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
calender= cal.month(year, month)
print(f"Calendar for {cal.month_name[month]} {year}:\n{calender}")
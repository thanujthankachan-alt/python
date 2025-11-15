import calendar

year = int(input("Enter the year: "))

# Check if it is a leap year
leap_year = calendar.isleap(year)

if leap_year:
    print("The given year is a leap year")
else:
    print("The given year is a non-leap year")

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter - Dec Jan Feb Mar
#                                dec 21 to 31 and mar 1 to 19
#      Mar 20 - Jun 20: Spring - Mar Apr May Jun
#                                mar 20 to 31 and jun 1 to 20
#      Jun 21 - Sep 21: Summer - Jun Jul Aug Sep
#                                jun 21 to 30 and sep 1 to 21
#      Sep 22 - Dec 20: Fall - Sep Oct Nov Dec
#                                sep 22 to 30 and dec 1 to 20
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec): ').lower()
day = int(input('Enter the day of the month: '))

winter = ['dec', 'jan', 'feb', 'mar']
spring = ['mar', 'apr', 'may', 'jun']
summer = ['jun', 'jul', 'aug', 'sep']
fall = ['sep', 'oct', 'nov', 'dec']

season = None

if month in winter: season = 'winter'
elif month in spring: season = 'spring'
elif month in fall: season = 'fall'
elif month in summer: season = 'summer'
else: print('Not a valid input')

if (month == 'dec' and day in range(21, 31)) or (month == 'mar' and day in range(1, 20)):
    season = 'winter'
elif (month == 'mar' and day in range(20, 32)) or (month == 'jun' and day in range(1, 21)):
    season = 'spring'
elif (month == 'jun' and day in range(21, 31)) or (month == 'sep' and day in range(1, 22)):
    season = 'summer'
elif (month == 'sep' and day in range(22, 31)) or (month == 'dec' and day in range(1, 21)):
    season = 'fall'
else:
    print('Not a valid input(s)')

print(f'{month} {day} is in {season}')
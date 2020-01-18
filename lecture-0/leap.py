year = int(input('Enter year: '))
if year % 4 != 0:
    print('Non-leap year')
elif year % 100 == 0 and year % 400 != 0:
    print('Usual year')
else:
    print('Leap year')
    
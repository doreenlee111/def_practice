def year(number):
	number = int(number)
	if number % 4 != 0:
		return False
	elif number % 4 == 0 and number%100 != 0:
		return True
	elif number % 100 == 0 and number%400 !=0:
		return False
	elif number % 400 == 0 and number %3200 != 0:
		return True
	else:
		return 'don\'t know'

y = input('please input year')
print(year(y))
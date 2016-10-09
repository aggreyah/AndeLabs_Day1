def fizz_buzz(arg):
	if (arg % 3 == 0) and (arg % 5 != 0):
		return 'Fizz'

	elif (arg % 3 == 0) and (arg % 5 == 0):
		return 'FizzBuzz'

	elif (arg % 3 != 0) and (arg % 5 == 0):
		return 'Buzz'

	else:
		return arg
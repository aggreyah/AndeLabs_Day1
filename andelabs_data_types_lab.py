def data_type(arg):
	""" A function that takes an argument,
	    compares and returns results based
	    on the argument supplied to the function
	    """
	if type(arg) == str:
		return len(arg)

	if arg == None:
		return 'no value'

	if type(arg) == bool:
		return arg

	if type(arg) == int:
		if arg < 100:
			return 'less than 100'
		elif arg == 100:
			print 'equal to 100'
			return None
		else:
			return 'more than 100'

	if type(arg) == list:
		t = arg[2:3]
		if t:
			return t[0]
		else:
			return None
def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='Run a single job')
	for argument in arguments:
		parser.add_argument(argument)
	return parser.parse_args()
def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='A simple tool to generate a random password')
	for argument in arguments:
		parser.add_argument(argument[0], help=argument[1])
	return parser.parse_args()
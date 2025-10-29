def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='Run a single command')
	parser.add_argument('command', nargs=1, help='The command to run')
	return parser.parse_args(arguments)
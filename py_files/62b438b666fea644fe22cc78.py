def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='Generate a random password')
	parser.add_argument('-l', '--length', type=int, default=12, help='The length of the generated password')
	parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols in the generated password')
	parser.add_argument('-n', '--numbers', action='store_true', help='Include numbers in the generated password')
	parser.add_argument('-c', '--characters', action='store_true', help='Include characters in the generated password')
	parser.add_argument('-d', '--digits', action='store_true', help='Include digits in the generated password')
	parser.add_argument('-p', '--password', action='store_true', help='Print the generated password to stdout')
	parser.add_argument('-f', '--file', action='store', help='Write the generated password to a file')
	parser.add_argument('-o', '--overwrite', action='store_true', help='Overwrite the contents of the specified file if it already exists')
	parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
	return parser.parse_args(arguments)
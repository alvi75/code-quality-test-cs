def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser(description='A simple tool to parse arguments')
	parser.add_argument('command', help='The command to run')
	parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose output')
	parser.add_argument('--version', action='store_true', help='Print version information')
	parser.add_argument('-h', '--help', action='store_true', help='Show this help message')

	return parser.parse_args(unparsed_arguments)
def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='Converts a file from the old format to the new format')
	parser.add_argument('input', help="The input file (in the old format)")
	parser.add_argument('output', help="The output file (in the new format)")
	parser.add_argument('-v', '--verbose', action='store_true', help="Verbose mode")
	return parser.parse_args(arguments)
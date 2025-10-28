def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='A tool to generate a list of files that can be used for testing')
	parser.add_argument('files', nargs='+',
						help='The file(s) to process')
	parser.add_argument('-o', '--output', default=sys.stdout,
						type=argparse.FileType('w'),
						help='Output file (default: stdout)')
	args = parser.parse_args(arguments)
	return args
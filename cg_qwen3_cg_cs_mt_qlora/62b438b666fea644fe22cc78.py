def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description="This script will generate a list of all the files in a directory that match a regular expression")
	parser.add_argument("directory", help="The directory to search for files matching the regular expression")
	parser.add_argument("regex", help="The regular expression to use to match files in the directory")
	parser.add_argument("-o", "--output", help="The output file to write the results to (defaults to stdout)", default=sys.stdout)
	return parser.parse_args(arguments)
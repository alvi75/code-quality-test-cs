def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description="A simple tool to generate a list of all the files in a directory and its subdirectories.")
	parser.add_argument("directory", help="The directory to search for files")
	parser.add_argument("-o", "--output", default=None, help="The output file to write the results to. If not specified, the results will be printed to stdout.")
	parser.add_argument("--recursive", action="store_true", help="Whether or not to recursively search through subdirectories")
	parser.add_argument("--include-hidden", action="store_true", help="Whether or not to include hidden files (files that start with .)")
	parser.add_argument("--exclude-patterns", nargs="+", help="A list of patterns to exclude from the search. For example: --exclude-patterns *.pyc --exclude-patterns *.swp")
	parser.add_argument("--include-patterns", nargs="+", help="A list of patterns to include in the search. For example: --include-patterns *.py --include-patterns *.txt")
	return parser.parse_args(arguments)
def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description="A tool to generate a list of all files in a directory tree.")
	parser.add_argument("directory", help="The directory from which to start searching for files")
	parser.add_argument("-f", "--file-extension", default="", help="Only include files that end with this extension (e.g. .py)")
	parser.add_argument("-s", "--sort-by-size", action="store_true", help="Sort by file size")
	parser.add_argument("-l", "--long-format", action="store_true", help="Print long format information about each file")
	return parser.parse_args(arguments)
def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""

	parser = argparse.ArgumentParser(description='A tool to generate a list of files that should be included in a tarball')

	parser.add_argument('-f', '--file', dest='files', action='append',
						help="The file(s) to include in the tarball")

	parser.add_argument('-d', '--directory', dest='directories', action='append',
						help="The directory(s) to include in the tarball")

	parser.add_argument('-e', '--exclude', dest='excludes', action='append',
						help="Files or directories to exclude from the tarball")

	parser.add_argument('-x', '--exclude-directory', dest='exclude_directories', action='append',
						help="Directories to exclude from the tarball")

	parser.add_argument('-o', '--output-file', dest='output_file', help="The output file for the tarball")

	args = parser.parse_args(arguments)

	return args
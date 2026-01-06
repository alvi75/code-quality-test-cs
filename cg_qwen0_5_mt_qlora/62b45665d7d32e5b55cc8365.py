def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser(description='Parse arguments')
	parser.add_argument('-v', '--verbose', action='store_true',
						help='Verbose output')
	parser.add_argument('-q', '--quiet', action='store_true',
						help='Quiet output')
	parser.add_argument('-d', '--debug', action='store_true',
						help='Debug output')
	parser.add_argument('-f', '--file', type=str, default=None,
						help='File to read from')
	parser.add_argument('-t', '--type', type=str, default=None,
						help='Type of file to read from')
	parser.add_argument('-s', '--size', type=int, default=0,
						help='Size of file to read from')
	parser.add_argument('-n', '--number', type=int, default=1,
						help='Number of files to read from')
	parser.add_argument('-o', '--output', type=str, default=None,
						help='Output file to write to')
	parser.add_argument('-i', '--input', type=str, default=None,
						help='Input file to read from')
	parser.add_argument('-r', '--read', type=str, default=None,
						help='Read file to read from')
	parser.add_argument('-w', '--write', type=str, default=None,
						help='Write file to')
	parser.add_argument('-c', '--count', type=int, default=0,
						help='Count of lines to read from')
	parser.add_argument('-l', '--list', action='store_true',
						help='List available files')
	parser.add_argument('-p', '--pattern', type=str, default=None,
						help='Pattern to match against files')
	parser.add_argument('-x', '--exclude', type=str, default=None,
						help='Exclude pattern to match against files')
	parser.add_argument('-e', '--error', action='store_true',
						help='Error output')
	parser.add_argument('-y', '--yes', action='store_true',
						help='Yes output')
	parser.add_argument('-z', '--zero', action='store_true',
						help='Zero output')
	parser.add_argument('-g', '--group', action='store_true',
						help='Group output')
	parser.add_argument('-a', '--all', action='store_true',
						help='All output')
	parser.add_argument('-b', '--block', action='store_true',
						help='Block output')
	parser.add_argument('-m', '--match', action
def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', '-i', help='Input file', required=True)
	parser.add_argument('--output', '-o', help='Output file', required=True)
	parser.add_argument('--format', '-f', help='Output format', required=True)
	parser.add_argument('--verbose', '-v', help='Verbose output', action='store_true')
	parser.add_argument('--debug', '-d', help='Debug output', action='store_true')
	parser.add_argument('--version', '-V', help='Version', action='store_true')
	parser.add_argument('--help', '-h', help='Help', action='store_true')
	args = parser.parse_args(unparsed_arguments)
	return args
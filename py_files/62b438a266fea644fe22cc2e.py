def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description='Converts a JSON file into a YAML file.')
	global_parser = parser.add_argument_group('Global options')
	global_parser.add_argument('--version', action='version',
		version='%(prog)s ' + __version__)
	global_parser.add_argument('-o', '--output-file', type=str,
		default=None, help='YAML output file')
	global_parser.add_argument('-i', '--input-file', type=str,
		default=None, help='JSON input file')

	subparsers = parser.add_subparsers(dest='subparser_name')

	def _add_subparser(subparser):
		for arg in ('--', '-'):
			subparser.add_argument(arg, dest=arg)
	return vars(parser.parse_known_args(unparsed_arguments))
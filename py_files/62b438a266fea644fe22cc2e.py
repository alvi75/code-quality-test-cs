def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
	dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description='Run a single command.')
	subparsers = parser.add_subparsers()
	for subparser_name in sorted(subparsers._actions_with_defaults.keys()):
		subparser = subparsers[subparser_name]
		subparser.set_defaults(func=parse_arguments)
		subparser.add_argument('command', nargs='?', help='The command to run')
		subparser.add_argument('-v', '--verbose', action='count', default=0,
			help='Increase verbosity of output')
		subparser.add_argument('--debug', action='store_true',
			help='Enable debug mode')
	return parser.parse_args(unparsed_arguments)
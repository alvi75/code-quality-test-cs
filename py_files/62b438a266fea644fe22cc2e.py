def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a single test or all tests in a directory.")
	subparsers = parser.add_subparsers(dest='subcommand')
	for subparser_name, subparser_class in SUBPARSER_CLASSES.items():
		subparser = subparsers.add_parser(subparser_name, help=subparser_class.__doc__.splitlines()[0])
		subparser.set_defaults(func=subparser_class)
		if hasattr(subparser_class, 'add_arguments'):
			subparser_class.add_arguments(subparser)

	args = vars(parser.parse_args(unparsed_arguments))
	return args
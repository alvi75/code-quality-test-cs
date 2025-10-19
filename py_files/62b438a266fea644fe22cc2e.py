def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest='subparser_name')
	for name in _get_subparsers():
		subparser = subparsers.add_parser(name)
		subparser.set_defaults(subparser_name=name)

	return vars(parser.parse_args(unparsed_arguments))
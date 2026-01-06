def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser()
	for unparsed_argument in unparsed_arguments:
		if isinstance(unparsed_argument, argparse.Namespace):
			parser.add_argument(**unparsed_argument.__dict__)
		else:
			parser.add_argument(*unparsed_argument.split(), **{'help': unparsed_argument})
	return parser.parse_args()
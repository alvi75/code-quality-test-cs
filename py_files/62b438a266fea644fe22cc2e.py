def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
 them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description='A simple tool for parsing command line arguments.')
	for arg in unparsed_arguments:
		parser.add_argument(arg[0], help=arg[1])
	return vars(parser.parse_args())
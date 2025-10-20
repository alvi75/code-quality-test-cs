def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
	them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""

	if len(unparsed_arguments) == 0:
		return {}

	parsed = {}
	for unparsed in unparsed_arguments:
		try:
			args = _parse_args(unparsed)
		except SystemExit:
			pass
		else:
			for key, value in args.items():
				if isinstance(value, list):
					value = ",".join(value)
				parsed[key] = value

	return parsed
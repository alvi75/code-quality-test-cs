def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
	instance, give each requested action's subparser a shot at parsing all arguments. This allows
	common arguments like "--repository" to be shared across multiple subparsers.

	Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
	arguments, a list of remaining arguments not claimed by any subparser).
	"""
	result = {}
	remaining_args = []
	for arg in unparsed_arguments:
		if arg.startswith("--"):
			arg_name = arg[2:]
			if "=" in arg_name:
				name, value = arg_name.split("=", 1)
				value = value.strip()
			else:
				name = arg_name
				value = None

			if name == "help":
				continue

			subparser = subparsers.get(name)
			if subparser is None:
				raise ValueError(
					"Unrecognized argument: {}".format(arg))
			try:
				namespace = subparser.parse_known_args([arg], {})
			except SystemExit:
				pass
			else:
				result[name] = namespace[0]
				remaining_args.extend(namespace[1])
	return result, remaining_args
def _parse_args(subparser_name, args):
		subparser = subparsers[subparser_name]
		return subparser.parse_args(args)

	parsed_args = {}
	for subparser_name in sorted(subparsers.keys()):
		args = unparsed_arguments.copy()
		try:
			result = _parse_args(subparser_name, args)
		except SystemExit:
			raise
		except Exception as e:
			raise ValueError("Error parsing arguments for subparser %s: %s" % (subparser_name, str(e)))
		parsed_args[subparser_name] = result[0]
		unclaimed_args = result[1:]
		if unclaimed_args:
			parsed_args["unclaimed"] = unclaimed_args

	return parsed_args, unparsed_arguments
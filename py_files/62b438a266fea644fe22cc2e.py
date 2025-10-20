def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
 them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	args = []
	for arg in unparsed_arguments:
		if isinstance(arg, list):
			args.extend(arg)
		else:
			args.append(arg)

	parsed_args = {}
	current_subparser_name = None

	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest='subparser_name')
	for subparser in subparsers.choices.values():
		subparser.set_defaults(subparser_name=subparser.name)

	while args:
		arg = args.pop(0)
		if arg == '--':
			break
		elif arg.startswith('--'):
			key, value = arg[2:].split('=', 1)
			value = value.replace('\\', '\\\\').replace('"', '\\"')
			parsed_args.setdefault(current_subparser_name, {})[key] = value
		elif arg.startswith('-'):
			key = arg[1:]
			if key not in parsed_args[current_subparser_name]:
				parsed_args[current_subparser_name][key] = True
		else:
			current_subparser_name = arg
	return parsed_args
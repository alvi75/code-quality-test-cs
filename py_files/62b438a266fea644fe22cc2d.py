def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
	instance, give each requested action's subparser a shot at parsing all arguments. This allows
	common arguments like "--repository" to be shared across multiple subparsers.

	Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
	arguments, a list of remaining arguments not claimed by any subparser).
	"""
	# TODO: this is a hack for backwards compatibility with old versions of the CLI.
	# Once we drop support for python 2.6, remove it.
	unparsed_arguments = [x for x in unparsed_arguments if isinstance(x, str)]
	args = {}
	remaining_args = []
	for parser_name, subparser in iteritems(subparsers):
		subparser_args = {}
		for arg in subparser._actions:
			if arg.dest == "repository":
				arg_value = unparsed_arguments.pop(0)
				subparser_args[arg.dest] = arg_value
			elif arg.nargs > 1:
				continue
			else:
				subparser_args[arg.dest] = True

		if len(subparser_args) == 0:
			# If no args were passed to this subparser, then don't even bother trying to parse it.
			# The only way to get here is if there was a --help or similar option that didn't have
			# any arguments.
			pass
		else:
			args[subparser_name] = subparser_args
			remaining_args.extend(subparser_args.values())

	return (args, remaining_args)
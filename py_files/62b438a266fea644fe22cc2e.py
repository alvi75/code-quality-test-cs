def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a single test or all tests in a directory.")
	subparsers = parser.add_subparsers(dest="subcommand")

	# Add the global options
	add_global_options(parser)

	# Add the subcommands
	for subcommand in SUBCOMMANDS:
		subcommand.add_to_parser(subparsers)

	# Parse the arguments
	args = parser.parse_args(unparsed_arguments)
	if args.subcommand is None:
		parser.print_help()
		sys.exit(1)

	# Return the parsed arguments
	return {args.subcommand: args}
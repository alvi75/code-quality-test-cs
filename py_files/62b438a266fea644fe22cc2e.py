def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a single test or all tests in a directory.")
	subparsers = parser.add_subparsers(dest='subcommand')

	# Add the global options
	add_global_options(parser)

	# Add the test options
	add_test_options(parser)

	# Add the test suite options
	add_suite_options(parser)

	# Parse the arguments
	args = parser.parse_args(unparsed_arguments)
	if args.subcommand == 'test':
		return {'global': args, 'test': None}
	elif args.subcommand == 'suite':
		return {'global': args, 'suite': None}
	else:
		raise ValueError("Invalid subcommand: {}".format(args.subcommand))
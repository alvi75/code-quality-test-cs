def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--version", action="version", version=__version__)
	subparsers = parser.add_subparsers(dest="subparser_name")
	subparsers.required = True
	subparsers.add_parser("global", help="Global options")
	subparsers.add_parser("run", help="Run a job")
	subparsers.add_parser("list", help="List jobs")
	subparsers.add_parser("show", help="Show a job")
	subparsers.add_parser("delete", help="Delete a job")
	subparsers.add_parser("cancel", help="Cancel a job")
	subparsers.add_parser("status", help="Show the status of a job")
	subparsers.add_parser("log", help="Show the log of a job")
	subparsers.add_parser("config", help="Show the configuration of a job")
	subparsers.add_parser("update", help="Update a job")
	subparsers.add_parser("submit", help="Submit a job")
	subparsers.add_parser("submit-batch", help="Submit a batch of jobs")
	subparsers.add_parser("submit-batch-from-file", help="Submit a batch of jobs from a file")
	subparsers.add_parser("submit-batch-from-stdin", help="Submit a batch of jobs from stdin")
	subparsers.add_parser("submit-batch-from-directory", help="Submit a batch of jobs from a directory")
	subparsers.add_parser("submit-batch-from-directory-recursive", help="Submit a batch of jobs from a directory recursively")
	subparsers.add_parser("submit-batch-from-directory-recursive-flat", help="Submit a batch of jobs from a directory
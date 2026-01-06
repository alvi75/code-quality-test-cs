def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = ArgumentParser(description="Run a set of tests.")
	subparsers = parser.add_subparsers(dest='subcommand')
	global_parser = subparsers.add_parser('global', help='Global options.')
	global_parser.add_argument('--log-level', default='info', choices=['debug', 'info', 'warning', 'error'], help='Set the log level.')
	global_parser.add_argument('--log-file', default=None, help='Log to file instead of stdout/stderr.')
	global_parser.add_argument('--log-format', default='%(asctime)s %(levelname)-8s %(name)s: %(message)s', help='Log format string for logging.')
	global_parser.add_argument('--log-datefmt', default='%Y-%m-%d %H:%M:%S', help='Date/time format string for logging.')
	global_parser.add_argument('--log-stderr', action='store_true', help='Log to stderr in addition to the configured log file.')
	global_parser.add_argument('--log-stdout', action='store_true', help='Log to stdout in addition to the configured log file.')
	global_parser.add_argument('--log-rotate', action='store_true', help='Rotate the log file when it reaches 10% of its maximum size.')
	global_parser.add_argument('--log-maxsize', type=int, default=1024*1024*10, help='Maximum size of the log file before rotating.')
	global_parser.add_argument('--log-backups', type=int, default=5, help='Number of backup log files to keep after rotating.')
	global_parser.add_argument('--log-dir', default='/var/log', help='Directory to store log files in.')
	global_parser.add_argument('--log-filename', default='testrunner.log', help='Name of the log file.')
	global_parser.add_argument('--log-encoding', default='utf-8', help='Encoding to use for the log file.')
	global_parser.add_argument('--log-encoding-error', default='replace', help='Error handling mode for the log file.')
	global_parser.add_argument('--log-encoding-unicodeerrors', action='store_true', help='Use unicode errors for the log file.')
	global_parser.add_argument('--log-encoding-unicodeerrors-encoding', default='utf-8', help='Encoding to use for unicode errors in the
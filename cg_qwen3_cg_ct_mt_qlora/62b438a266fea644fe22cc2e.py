def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = argparse.ArgumentParser(description="Run a single test or all tests in a directory.")
	subparsers = parser.add_subparsers(dest="subcommand")

	# Add the global options
	global_parser = subparsers.add_parser("global", help="Global options")
	global_parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
	global_parser.add_argument("--debug", action="store_true", help="Enable debug output")
	global_parser.add_argument("--log-file", type=str, default=None, help="Log to file instead of stdout/stderr")
	global_parser.add_argument("--log-level", type=str, default="info", choices=["debug", "info", "warning", "error"], help="Set log level")
	global_parser.add_argument("--log-format", type=str, default="%(asctime)s %(levelname)s: %(message)s", help="Set log format")
	global_parser.add_argument("--log-datefmt", type=str, default="%Y-%m-%d %H:%M:%S", help="Set log date format")
	global_parser.add_argument("--log-encoding", type=str, default="utf-8", help="Set log encoding")
	global_parser.add_argument("--log-max-size", type=int, default=1024*1024*5, help="Maximum size of log file before rolling over")
	global_parser.add_argument("--log-backup-count", type=int, default=3, help="Number of backup files to keep when rolling over")
	global_parser.add_argument("--log-file-name", type=str, default="test.log", help="Name of log file")
	global_parser.add_argument("--log-file-dir", type=str, default=None, help="Directory for log file; if not specified, use current working directory")
	global_parser.add_argument("--log-file-rotation", type=str, default="size", choices=["size", "time"], help="Rotation mode for log file")
	global_parser.add_argument("--log-file-rotation-size", type=int, default=1024*1024*5, help="Size at which to rotate log file")
	global_parser.add_argument("--log-file-rotation-time", type=int, default=60*60, help="Time at which to rotate log file")
	global_parser.add_argument("--log
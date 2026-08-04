def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('--config', help='Path to config file')
	parser.add_argument('--log', help='Path to log file')
	parser.add_argument('--debug', help='Debug mode', action='store_true')
	parser.add_argument('--verbose', help='Verbose mode', action='store_true')
	parser.add_argument('--quiet', help='Quiet mode', action='store_true')
	parser.add_argument('--version', help='Show version', action='store_true')
	parser.add_argument('--help', help='Show help', action='store_true')
	parser.add_argument('--no-color', help='Disable color output', action='store_true')
	parser.add_argument('--no-banner', help='Disable banner', action='store_true')
	parser.add_argument('--no-progress', help='Disable progress bar', action='store_true')
	parser.add_argument('--no-spinner', help='Disable spinner', action='store_true')
	parser.add_argument('--no-prompt', help='Disable prompt', action='store_true')
	parser.add_argument('--no-confirm', help='Disable confirmation prompt', action='store_true')
	parser.add_argument('--no-input', help='Disable input prompt', action='store_true')
	parser.add_argument('--no-output', help='Disable output', action='store_true')
	parser.add_argument('--no-error', help='Disable error output', action='store_true')
	parser.add_argument('--no-warn', help='Disable warning output', action='store_true')
	parser.add_argument('--no-info', help='Disable info output', action='store_true')
	parser.add_argument('--no-debug', help='Disable debug output', action='store_true')
	parser.add_
def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='Run a command in a subprocess and wait for it to finish')
	parser.add_argument('--timeout', type=int, default=None, help='Timeout in seconds')
	parser.add_argument('--output', type=str, default=None, help='File to write output to')
	parser.add_argument('--error', type=str, default=None, help='File to write error output to')
	parser.add_argument('--input', type=str, default=None, help='File to read input from')
	parser.add_argument('--cwd', type=str, default=None, help='Working directory')
	parser.add_argument('--env', type=str, default=None, help='Environment variables to set')
	parser.add_argument('--shell', type=str, default=None, help='Shell to use')
	parser.add_argument('--shell-args', type=str, default=None, help='Shell arguments')
	parser.add_argument('--shell-env', type=str, default=None, help='Shell environment variables')
	parser.add_argument('--shell-cwd', type=str, default=None, help='Shell working directory')
	parser.add_argument('--shell-input', type=str, default=None, help='Shell input')
	parser.add_argument('--shell-output', type=str, default=None, help='Shell output')
	parser.add_argument('--shell-error', type=str, default=None, help='Shell error')
	parser.add_argument('--shell-env-file', type=str, default=None, help='Shell environment variables file')
	parser.add_argument('--shell-cwd-file', type=str, default=None, help='Shell working directory file')
	parser.add_argument('--shell-input-file', type=str, default=None, help='Shell input file')
	parser.add_argument('--shell-
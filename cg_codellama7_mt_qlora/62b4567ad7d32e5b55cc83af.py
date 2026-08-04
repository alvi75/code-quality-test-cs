def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='Generate a random password')
	parser.add_argument('-l', '--length', type=int, default=12, help='length of the password')
	parser.add_argument('-c', '--characters', type=str, default='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', help='characters to use in the password')
	parser.add_argument('-n', '--no-symbols', action='store_true', help='do not include symbols in the password')
	parser.add_argument('-s', '--symbols', type=str, default='!@#$%^&*()_+-=[]{}|;:<>,.?/~', help='symbols to use in the password')
	parser.add_argument('-u', '--uppercase', action='store_true', help='include uppercase characters in the password')
	parser.add_argument('-l', '--lowercase', action='store_true', help='include lowercase characters in the password')
	parser.add_argument('-d', '--digits', action='store_true', help='include digits in the password')
	parser.add_argument('-p', '--password', action='store_true', help='print the password to stdout')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
	parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
	return parser.parse_args(arguments)
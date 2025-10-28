def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description='A simple tool to generate a random password')
	parser.add_argument('-l', '--length', type=int, default=8,
						help='The length of the password (default: 8)')
	parser.add_argument('-n', '--numbers', action='store_true',
						help='Include numbers in the password (default: False)')
	parser.add_argument('-s', '--specials', action='store_true',
						help='Include special characters in the password (default: False)')
	parser.add_argument('-d', '--digits', action='store_true',
						help='Include digits in the password (default: False)')
	parser.add_argument('-a', '--alphabet', nargs='+',
						help='Specify custom alphabet for the password (default: ABCDEFGHIJKLMNOPQRSTUVWXYZ)')
	parser.add_argument('-u', '--uppercase', action='store_true',
						help='Include uppercase letters in the password (default: False)')
	parser.add_argument('-i', '--lowercase', action='store_true',
						help='Include lowercase letters in the password (default: False)')
	parser.add_argument('-o', '--other', action='store_true',
						help='Include other characters in the password (default: False)')

	return parser.parse_args(arguments)
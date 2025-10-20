def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description="A simple script to generate a random password")
	parser.add_argument("-l", "--length", type=int, default=12, help="The length of the password to generate (default: %(default)s)")
	parser.add_argument("-c", "--characters", nargs="+", default=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], help="The characters to use in the password (default: %(default)s)")
	parser.add_argument("-C", "--case", action="store_true", help="Include both upper- and lower-case letters in the password")
	parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers in the password")
	parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols in the password")
	return parser.parse_args(arguments)
def parse_arguments(*arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
	"""
	parser = argparse.ArgumentParser(description="A simple script to generate a random password")
	parser.add_argument("-l", "--length", type=int, default=12, help="The length of the generated password")
	parser.add_argument("-s", "--special", action="store_true", help="Include special characters in the generated password")
	parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers in the generated password")
	parser.add_argument("-c", "--characters", action="store_true", help="Include characters in the generated password")
	parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters in the generated password")
	parser.add_argument("-d", "--lowercase", action="store_true", help="Include lowercase letters in the generated password")
	parser.add_argument("-o", "--output", type=str, default=None, help="Output file for the generated password")
	return parser.parse_args(arguments)
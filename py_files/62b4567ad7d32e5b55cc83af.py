def parse_arguments(*arguments):
		"""
		Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance
		"""
		parser = argparse.ArgumentParser(description='A simple demonstration of a Yelp API client')
		parser.add_argument('--search', '-s', type=str, required=True,
			help='The search term to use in the Yelp API query.')
		parser.add_argument('--location', '-l', type=str, required=True,
			help='The location to use in the Yelp API query.')
		return parser.parse_args(arguments)
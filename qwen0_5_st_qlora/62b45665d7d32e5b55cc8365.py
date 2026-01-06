def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser()
	for arg in unparsed_arguments:
		parser.add_argument(arg)
	return vars(parser.parse_args())
def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	parser = argparse.ArgumentParser()
	for arg in unparsed_arguments:
		if isinstance(arg, str):
			parser.add_argument(arg)
		elif isinstance(arg, list):
			for item in arg:
				parser.add_argument(item)
		else:
			raise TypeError("Argument must be a string or list of strings")
	return vars(parser.parse_args())
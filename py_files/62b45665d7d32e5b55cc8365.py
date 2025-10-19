def parse_arguments(*unparsed_arguments):
		"""
		Parses parameters and returns them as dict maps
		"""
		args = {}
		for arg in unparsed_arguments:
			if isinstance(arg, list):
				arg = " ".join(arg)
			key, value = arg.split("=", 1)
			args[key] = value

		return args
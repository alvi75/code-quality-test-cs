def get_option_spec(self, command_name, argument_name):
	"""
	Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
	"""
	if not self._option_specs:
		self._load_option_specs()

	return self._option_specs.get((command_name, argument_name), None)
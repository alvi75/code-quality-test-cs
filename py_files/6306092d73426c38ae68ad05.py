def get_option_spec(self, command_name, argument_name):
	"""
	Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
	"""
	if not self._option_specs:
		self._parse_options()

	return self._option_specs[command_name][argument_name]
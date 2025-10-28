def get_option_spec(self, command_name, argument_name):
	"""
	Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
	"""
	if not isinstance(command_name, basestring) or not isinstance(argument_name, basestring):
		raise TypeError("command_name and argument_name must be strings")
	return self._parser_options[command_name][argument_name]
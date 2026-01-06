def get_option_spec(self, command_name, argument_name):
	"""
	Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
	"""
	for spec in self.get_parser_option_specs(command_name):
		if spec['name'] == argument_name:
			return spec
	raise ValueError('No such option: %s' % argument_name)
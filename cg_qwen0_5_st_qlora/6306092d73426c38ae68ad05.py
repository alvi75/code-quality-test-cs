def get_option_spec(self, command_name, argument_name):
	"""
	Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
	"""
	if not command_name in self.commands:
		raise ValueError("Command %s does not exist" % command_name)
	if not argument_name in self.commands[command_name].options:
		raise ValueError("Option %s does not exist" % argument_name)

	return self.commands[command_name].options[argument_name]
def get_option_spec(self, command_name, argument_name):
	"""
	Gets the specification for the specified option name. Get options of the given command_name with self.get_parser_option_specs()
	"""
	if not self.has_command(command_name):
		raise CommandError("Command '%s' does not exist" % command_name)
	return self._get_option_spec(command_name, argument_name)
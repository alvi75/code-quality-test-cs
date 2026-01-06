def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	if command_name not in self._parser_option_specs:
		self._parser_option_specs[command_name] = []
		for option in self._parser.get_option(command_name):
			self._parser_option_specs[command_name].append(option)
	return self._parser_option_specs[command_name]
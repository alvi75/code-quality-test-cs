def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	if not self._parser:
		self._init_parsers()
	return self._parser.get_options(command_name)
def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	options = []
	for option in self._parser.get_options():
		if option.dest == 'command' and option.name == command_name:
			options.append(option)
	return options
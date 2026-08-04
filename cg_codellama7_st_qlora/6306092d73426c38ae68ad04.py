def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	command_options = []
	for option in self.get_parser_options(command_name):
		command_options.append(option)
	return command_options
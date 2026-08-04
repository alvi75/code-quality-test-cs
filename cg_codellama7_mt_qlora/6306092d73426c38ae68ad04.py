def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	command_options = []
	for command in self.commands:
		if command.name == command_name:
			command_options = command.options
			break
	return command_options
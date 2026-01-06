def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	command = self.get_command(command_name)
	if not command:
		return []
	options = [o for o in command.options if o.name != 'help']
	return options
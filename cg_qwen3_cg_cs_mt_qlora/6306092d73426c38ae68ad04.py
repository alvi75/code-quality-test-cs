def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	if command_name not in self._parser_options:
		self._parser_options[command_name] = []
		for option in self._parser.get_option_list():
			if option.dest == 'cmd':
				continue
			if option.dest.startswith('cmd_'):
				continue
			if option.dest.startswith('cmd_{}'.format(command_name)):
				self._parser_options[command_name].append(option)
	return self._parser_options[command_name]
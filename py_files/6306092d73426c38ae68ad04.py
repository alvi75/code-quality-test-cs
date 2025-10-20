def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""

	if not self._parser_options:
			return []

	command = self.get_command(command_name)
	options = []
	for option in command.option_list:
		specs = {}
		specs['name'] = option.dest
		specs['help'] = option.help
		specs['default'] = option.default
		specs['action'] = option.action
		specs['type'] = option.type
		specs['choices'] = option.choices
		specs['required'] = option.required
		specs['metavar'] = option.metavar
		specs['dest'] = option.dest
		specs['nargs'] = option.nargs
		specs['const'] = option.const
		specs['count'] = option.count
		specs['allow_from_takes'] = option.allow_from_takes
		specs['envvar_prefix'] = option.envvar_prefix
		specs['help'] = option.help
		specs['metavar'] = option.metavar
		specs['type'] = option.type
		specs['choices'] = option.choices
		specs['required'] = option.required
		specs['count'] = option.count
		specs['allow_from_takes'] = option.allow_from_takes
		specs['envvar_prefix'] = option.envvar_prefix
		specs['help'] = option.help
		specs['metavar'] = option.metavar
		specs['type'] = option.type
		specs['choices'] = option.choices
		specs['required'] = option.required
		specs['count'] = option.count
		specs['allow_from_takes'] = option.allow_from_takes
		specs['envvar_prefix'] = option.envvar_prefix
		specs['help'] = option.help
		specs['metavar'] = option.metavar
		specs['type'] = option.type
		specs['choices'] = option.choices
		specs['required'] = option.required
		specs['count'] = option.count
		specs['allow_from_takes'] = option.allow_from_takes
		specs['envvar_prefix'] = option.envvar
def get_parser_option_specs(self, command_name):
	"""
	Gets all the options for the specified command

:param command_name: the command name (main, virsh, ospd, etc...)
:return: the list of all command options
	"""
	if not self._parser_options:
			return []
		command = self._parser_options.get(command_name)
		if not command:
			return []

		options = []
		for option in command.option_list:
			specs = {}
			specs['name'] = option.name
			specs['short_name'] = option.short_name
			specs['long_name'] = option.long_name
			specs['description'] = option.description
			specs['type'] = option.type
			specs['default_value'] = option.default_value
			specs['required'] = option.required
			specs['choices'] = option.choices
			specs['validator'] = option.validator
			specs['help'] = option.help
			specs['action'] = option.action
			specs['nargs'] = option.nargs
			specs['const'] = option.const
			specs['dest'] = option.dest
			specs['metavar'] = option.metavar
			specs['count'] = option.count
			specs['is_flag'] = option.is_flag
			specs['flag_value'] = option.flag_value
			specs['flag_help'] = option.flag_help
			specs['flag_required'] = option.flag_required
			specs['flag_choices'] = option.flag_choices
			specs['flag_validator'] = option.flag_validator
			specs['flag_help'] = option.flag_help
			specs['flag_action'] = option.flag_action
			specs['flag_nargs'] = option.flag_nargs
			specs['flag_const'] = option.flag_const
			specs['flag_dest'] = option.flag_dest
			specs['flag_metavar'] = option.flag_metavar
			specs['flag_count'] = option.flag_count
			specs['flag_is_flag'] = option.flag_is_flag
			specs['flag_flag_value'] = option.flag_flag_value
			specs['flag_flag_help'] = option.flag_flag_help
			specs['flag_flag_required'] = option.flag_flag_required
			specs['flag_flag_choices'] = option.flag_flag_choices
			specs['flag_flag_validator'] = option.flag_flag_validator
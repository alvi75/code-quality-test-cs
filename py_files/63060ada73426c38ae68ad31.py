def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if parser_name == 'main':
		values_dict['verbose'] = bool(values_dict['verbose'])
		values_dict['debug'] = bool(values_dict['debug'])
		values_dict['log_file'] = str(values_dict['log_file'])
		values_dict['log_level'] = int(values_dict['log_level'])

	elif parser_name == 'virsh':
		values_dict['virsh_command'] = str(values_dict['virsh_command'])
		values_dict['virsh_args'] = str(values_dict['virsh_args'])
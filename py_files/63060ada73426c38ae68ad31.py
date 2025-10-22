def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.
	
:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if parser_name == 'main':
		values_dict['verbose'] = self._get_verbose_level(values_dict['verbose'])
		values_dict['debug'] = self._get_debug_level(values_dict['debug'])

	if parser_name in ['virsh', 'ospd']:
		values_dict['timeout'] = int(values_dict['timeout'])
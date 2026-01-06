def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	for key in list(values_dict.keys()):
		if key == 'name':
			values_dict[key] = self._convert_to_string(values_dict['name'])
		elif key == 'type':
			values_dict[key] = self._convert_to_string(values_dict['type'])
		elif key == 'value':
			values_dict[key] = self._convert_to_string(values_dict['value'])

	return values_dict
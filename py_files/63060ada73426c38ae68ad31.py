def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	for key in list(values_dict.keys()):
		if key == 'config':
			values_dict[key] = self._convert_config_to_dict(values_dict[key])
		elif key == 'name':
			values_dict[key] = self._convert_name_to_dict(values_dict[key])
		elif key == 'type':
			values_dict[key] = self._convert_type_to_dict(values_dict[key])
		elif key == 'value':
			values_dict[key] = self._convert_value_to_dict(values_dict[key])
		else:
			values_dict[key] = str(values_dict[key])

	return values_dict
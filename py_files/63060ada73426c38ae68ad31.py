def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	for key in values_dict:
		if key == 'port':
			values_dict[key] = int(values_dict[key])
		elif key == 'timeout':
			values_dict[key] = float(values_dict[key])
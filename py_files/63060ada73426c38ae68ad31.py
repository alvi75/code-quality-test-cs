def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	for key in values_dict:
		if isinstance(values_dict[key], str) or \
				not isinstance(values_dict[key], (list, tuple)):
			values_dict[key] = [values_dict[key]]
		elif isinstance(values_dict[key], list):
			for i in range(len(values_dict[key])):
				values_dict[key][i] = self._cast_to_type(parser_name,
				                                     values_dict[key][i])
	return values_dict
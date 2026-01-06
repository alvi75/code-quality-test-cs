def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	for key in list(values_dict.keys()):
		if key not in self._cli_args:
			continue

		if isinstance(values_dict[key], str):
			values_dict[key] = self._cli_args[key](values_dict[key])
		elif isinstance(values_dict[key], int):
			values_dict[key] = self._cli_args[key](int(values_dict[key]))
		elif isinstance(values_dict[key], float):
			values_dict[key] = self._cli_args[key](float(values_dict[key]))
		elif isinstance(values_dict[key], bool):
			values_dict[key] = self._cli_args[key](bool(values_dict[key]))
		else:
			raise ValueError("Unknown type for argument %s" % key)
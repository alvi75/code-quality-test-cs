def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	for key in self._non_cli_args[parser_name]:
		if key in values_dict:
			values_dict[key] = self._non_cli_args[parser_name][key](values_dict[key])
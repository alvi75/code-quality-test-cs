def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if not self._cli:
		return

	for key in values_dict.keys():
		value = values_dict[key]
		if value is None or isinstance(value, bool) or isinstance(value, int):
			continue

		try:
			values_dict[key] = self._get_type(parser_name)(value)
		except ValueError as err:
			raise CliError("Invalid argument for %s: %s" % (parser_name, str(err)))
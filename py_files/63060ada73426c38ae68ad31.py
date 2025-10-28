def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if not self._cli:
		return

	for arg in self._cli.get_parser(parser_name).arguments:
		if isinstance(arg.type, type) and issubclass(arg.type, str):
			continue

		values_dict[arg.dest] = self._convert_type(values_dict[arg.dest], arg.type)

	return values_dict
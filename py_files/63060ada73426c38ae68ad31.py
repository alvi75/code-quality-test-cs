def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if not self._cli:
		return

	for arg in self._non_cli_args[parser_name]:
		try:
			values_dict[arg] = self._cli.convert_arg(arg, values_dict[arg])
		except ValueError as ex:
			raise CLIError("Invalid value for argument '%s': %s" % (arg, str(ex)))
def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""
	if parser_name in self.non_cli_args_converters:
		for arg_name, converter in self.non_cli_args_converters[parser_name].items():
			if arg_name in values_dict:
				values_dict[arg_name] = converter(values_dict[arg_name])
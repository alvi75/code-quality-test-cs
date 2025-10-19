def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if parser_name == 'main':
		return

	parser = self._parsers[parser_name]
	for arg in parser.args:
		arg_type = arg.type
		if not arg_type:
			continue

		if arg.dest in values_dict:
			value = values_dict[arg.dest]

			try:
				if arg_type is int:
					value = int(value)
				elif arg_type is float:
					value = float(value)
				elif arg_type is bool:
					value = (value.lower() == 'true')
				elif arg_type is list:
					value = value.split(',')
				values_dict[arg.dest] = value
			except ValueError as ex:
				raise ValueError("Argument %s has invalid type (%s): %s" % (arg.dest, arg_type.__name__, str(ex)))
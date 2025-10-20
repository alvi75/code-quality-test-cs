def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if parser_name == 'main':
		values_dict['verbose'] = int(values_dict['verbose'])
		values_dict['debug'] = int(values_dict['debug'])

	elif parser_name == 'virsh':
		values_dict['timeout'] = int(values_dict['timeout'])
		values_dict['max_retries'] = int(values_dict['max_retries'])
		values_dict['interval'] = int(values_dict['interval'])
		values_dict['wait_for'] = int(values_dict['wait_for'])
		values_dict['wait_for'] = int(values_dict['wait_for'])
		values_dict['wait_for'] = int(values_dict['wait_for'])
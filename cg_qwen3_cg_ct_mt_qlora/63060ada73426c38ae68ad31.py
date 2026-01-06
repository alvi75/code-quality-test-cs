def _convert_non_cli_args(self, parser_name, values_dict):
	"""
	Casts arguments to correct types by modifying values_dict param.

By default all the values are strings.

:param parser_name: The command name, e.g. main, virsh, ospd, etc
:param values_dict: The dict of with arguments
	"""

	if parser_name == 'main':
		values_dict['verbose'] = bool(values_dict['verbose'])
		values_dict['debug'] = bool(values_dict['debug'])

	elif parser_name == 'ospd':
		values_dict['port'] = int(values_dict['port'])
		values_dict['timeout'] = int(values_dict['timeout'])
		values_dict['max_connections'] = int(values_dict['max_connections'])
		values_dict['max_requests'] = int(values_dict['max_requests'])
		values_dict['max_threads'] = int(values_dict['max_threads'])
		values_dict['max_concurrent'] = int(values_dict['max_concurrent'])
		values_dict['max_concurrent_per_host'] = int(
			values_dict['max_concurrent_per_host']
		)
		values_dict['max_concurrent_per_user'] = int(
			values_dict['max_concurrent_per_user']
		)

	elif parser_name == 'virsh':
		values_dict['timeout'] = int(values_dict['timeout'])
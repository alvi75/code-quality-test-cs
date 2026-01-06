def _replace_register(flow_params, register_number, register_value):
	"""
	Replace the value of flow_params[register_number] with flow_params[register_value] and delete flow_params[register_value]
	"""
	if isinstance(register_value, int) or isinstance(register_value, float):
		return {k: v for k, v in six.iteritems(flow_params) if k != register_number}
	else:
		return {k: v for k, v in six.iteritems(flow_params) if k != register_value}
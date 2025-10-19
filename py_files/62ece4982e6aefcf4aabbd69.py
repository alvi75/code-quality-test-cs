def _replace_register(flow_params, register_number, register_value):
	"""
	Replace the value of flow_params[register_number] with flow_params[register_value] and delete flow_params[register_value]
	"""
	if register_number in flow_params:
		flow_params[register_number] = flow_params[register_value]
	else:
		raise ValueError("Register number %d not found" % register_number)
	del flow_params[register_value]
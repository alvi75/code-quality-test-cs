def create_complex_argumet_type(self, subcommand, type_name, option_name, spec_option):
	"""
	Returns the corresponding function in COMPLEX_TYPES based on type_name and returns the result obtained by complex_action after option_name,(self.vars, self.defaults, self.plugin_path), subcommand, spec_option) is input.
	"""
	
	if type_name == "int":
		return lambda vars, defaults, plugin_path: int(vars[type_name])
	elif type_name == "float":
		return lambda vars, defaults, plugin_path: float(vars[type_name])
	else:
		return lambda vars, defaults, plugin_path: str(vars[type_name])
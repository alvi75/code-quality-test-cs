def create_complex_argumet_type(self, subcommand, type_name, option_name, spec_option):
	"""
	Returns the corresponding function in COMPLEX_TYPES based on type_name and returns the result obtained by complex_action after option_name,(self.vars, self.defaults, self.plugin_path), subcommand, spec_option) is input.
	"""
	def complex_action(vars, defaults, plugin_path):
		return COMPLEX_TYPES[type_name](vars, defaults, plugin_path, subcommand, spec_option)
	return complex_action
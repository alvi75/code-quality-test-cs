def create_complex_argumet_type(self, subcommand, type_name, option_name,
									spec_option):
		"""
	Returns the corresponding function in COMPLEX_TYPES based on type_name and returns the result obtained by complex_action after option_name,(self.vars, self.defaults, self.plugin_path), subcommand, spec_option) is input.
		"""
		if type_name == 'string':
			return self.create_string_argumet_type(subcommand, option_name, spec_option)
		elif type_name == 'integer':
			return self.create_integer_argumet_type(subcommand, option_name, spec_option)
		elif type_name == 'float':
			return self.create_float_argumet_type(subcommand, option_name, spec_option)
		elif type_name == 'boolean':
			return self.create_boolean_argumet_type(subcommand, option_name, spec_option)
		else:
			raise Exception('Unknown type name: %s' % type_name)
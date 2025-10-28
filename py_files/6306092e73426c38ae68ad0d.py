def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                     spec_option):
	"""
	Returns the corresponding function in COMPLEX_TYPES based on type_name and returns the result obtained by complex_action after option_name,(self.vars, self.defaults, self.plugin_path), subcommand, spec_option) is input.
	"""
	if type_name == 'file':
		return self.create_file_argument_type(subcommand, option_name)
	elif type_name == 'directory':
		return self.create_directory_argument_type(subcommand, option_name)
	elif type_name == 'path':
		return self.create_path_argument_type(subcommand, option_name)
	elif type_name == 'string':
		return self.create_string_argument_type(subcommand, option_name)
	elif type_name == 'integer':
		return self.create_integer_argument_type(subcommand, option_name)
	elif type_name == 'boolean':
		return self.create_boolean_argument_type(subcommand, option_name)
	else:
		raise ValueError('Unknown argument type: %s' % type_name)
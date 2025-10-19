def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                   spec_option):
	"""
	Returns the corresponding function in COMPLEX_TYPES based on type_name and returns the result obtained by complex_action after option_name,(self.vars, self.defaults, self.plugin_path), subcommand, spec_option) is input.
	"""
	if not type_name:
		return None

	type_name = type_name.lower()
	if type_name == "list":
		return self.create_list_argument(subcommand, option_name, spec_option)
	elif type_name == "dict":
		return self.create_dict_argument(subcommand, option_name, spec_option)
	elif type_name == "tuple" or type_name == "tuple2":
		return self.create_tuple_argument(subcommand, option_name, spec_option)

	# If it's a complex type, we need to call the corresponding action
	complex_action = getattr(self, "complex_action_" + type_name)
	return complex_action((self.vars, self.defaults, self.plugin_path),
	                      subcommand, spec_option)
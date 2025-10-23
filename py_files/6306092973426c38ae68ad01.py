def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	deprecation_dict = {}
	for option_spec in self.spec_helper.iterate_option_specs():
		if 'deprecated' in option_spec:
			deprecation_dict[option_spec['name']] = option_spec['deprecated']
	return deprecation_dict
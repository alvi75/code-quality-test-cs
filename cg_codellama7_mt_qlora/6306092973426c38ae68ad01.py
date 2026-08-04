def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	deprecated_args = {}
	for option_spec in self.spec_helper.iterate_option_specs():
		if option_spec.deprecated_by:
			deprecated_args[option_spec.name] = option_spec.deprecated_by
	return deprecated_args
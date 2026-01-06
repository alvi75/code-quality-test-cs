def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	deprecations = {}
	for option in self.spec_helper.iterate_option_specs():
		if option.deprecation is not None:
			deprecations[option.name] = option.deprecation
	return deprecations
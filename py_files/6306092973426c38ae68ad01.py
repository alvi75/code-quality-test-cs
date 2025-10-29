def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	deprecation = {}
	for option in self.spec_helper.iterate_option_specs():
		if option.deprecated:
			deprecation[option.name] = option.deprecated
	return deprecation
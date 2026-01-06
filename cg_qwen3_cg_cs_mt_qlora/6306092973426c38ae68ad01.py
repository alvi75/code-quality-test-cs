def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	depr = {}
	for opt in self.spec_helper.iterate_option_specs():
		if opt.deprecated:
			depr[opt.name] = opt.deprecated
	return depr
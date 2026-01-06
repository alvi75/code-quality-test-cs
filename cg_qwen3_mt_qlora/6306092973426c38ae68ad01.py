def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	depr_options = {}
	for option in self.spec_helper.iterate_option_specs():
		if option.deprecated:
			if option.deprecated in depr_options:
				depr_options[option.deprecated].append(option)
			else:
				depr_options[option.deprecated] = [option]
	return depr_options
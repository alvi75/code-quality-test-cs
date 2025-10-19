def get_deprecated_args(self):
	"""
	Returning dict with options which deprecate others. options from self.spec_helper.iterate_option_specs()
	"""
	ret = {}
	for o in self.spec_helper.iterate_option_specs():
		if 'deprecated' not in o:
			continue

		deprecated = o['deprecated']
		if isinstance(deprecated, list):
			for d in deprecated:
				ret[d] = o
		else:
			ret[deprecated] = o

	return ret
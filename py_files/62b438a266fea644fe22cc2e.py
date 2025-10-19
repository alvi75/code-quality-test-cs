def parse_arguments(*unparsed_arguments):
	"""
	Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
	"""
	parser = create_parser()
	args = parser.parse_args(unparsed_arguments)
	result = {}
	def recurse(namespace, prefix):
		if not hasattr(namespace, 'items'):
			return
		for k,v in namespace.items():
			if isinstance(v, argparse.Namespace):
				prefixed_key = '%s_%s' % (prefix, k) if prefix else k
				result[prefixed_key] = v
				recurse(v, prefixed_key)
			else:
				result[prefix] = namespace
	recurse(args, '')
	return result
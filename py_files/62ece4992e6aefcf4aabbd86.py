def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""
	if not isinstance(obj, str):
		return None
	return yaml.dump(obj, Dumper=dumper)
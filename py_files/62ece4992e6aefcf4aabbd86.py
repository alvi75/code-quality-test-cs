def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""

	if isinstance(obj, six.string_types):
		return obj
	elif isinstance(obj, dict):
		return dumper(dump(obj), default_flow_style=False)
	elif isinstance(obj, list):
		return dumper(dump(obj), default_flow_style=False)
	else:
		raise TypeError("Can't dump %s" % type(obj))
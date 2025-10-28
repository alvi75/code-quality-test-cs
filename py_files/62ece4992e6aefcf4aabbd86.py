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

	if isinstance(obj, (list, tuple)):
		return [yaml.dump(item, dumper=dumper) for item in obj]

	if isinstance(obj, dict):
		return {key: yaml.dump(value, dumper=dumper) for key, value in obj.items()}

	raise TypeError("Cannot dump type %s" % type(obj))
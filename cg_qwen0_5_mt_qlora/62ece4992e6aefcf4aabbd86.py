def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""
	if isinstance(obj, six.string_types):
		return dumper.represent_scalar('tag:yaml.org,2002:str', obj)
	elif isinstance(obj, bool):
		return dumper.represent_scalar('tag:yaml.org,2002:bool', obj)
	elif isinstance(obj, bytes):
		return dumper.represent_scalar('tag:yaml.org,2002:str', obj.decode('utf-8'))
	elif isinstance(obj, dict):
		return dumper.represent_mapping('tag:yaml.org,2002:dct', obj)
	elif isinstance(obj, list):
		return dumper.represent_list('tag:yaml.org,2002:lst', obj)
	else:
		raise TypeError("Can't dump type %s" % type(obj))
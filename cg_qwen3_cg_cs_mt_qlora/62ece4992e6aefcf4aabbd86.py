def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""
	if dumper is None:
		dumper = yaml.Dumper
	def _represent_python_object(dumper, data):
		return dumper.represent_mapping('tag:yaml.org,2002:python/object', (data.__class__.__module__, data.__class__.__name__), dict(data.__dict__))
	dumper.add_representer(type(obj), _represent_python_object)
	return dumper.dump(obj)
def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""
	if isinstance(obj, dict):
		return dumper.represent_dict(_dict_to_yaml(obj))
	elif isinstance(obj, list):
		return dumper.represent_list(_list_to_yaml(obj))
	else:
		return dumper.represent_scalar('tag:yaml.org,2002:str', str(obj))
def _dump_string(obj, dumper=None):
    """
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""
    if not isinstance(obj, dict) or 'id' in obj:
        return yaml.dump(obj)
    else:
        return yaml.dump({obj['id']: obj})
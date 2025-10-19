def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""

	if not dumper:
		dumper = Dumper

	return dumper(obj).encode('utf-8')
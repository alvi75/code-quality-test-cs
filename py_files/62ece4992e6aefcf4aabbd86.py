def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""

	if not isinstance(obj, dict) or 'type' in obj:
		return yaml.dump(obj)

	dumper = dumper if dumper else Dumper
	stream = StringIO()
	dumper.write(stream, obj)
	return stream.getvalue()
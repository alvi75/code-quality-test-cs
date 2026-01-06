def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""

	if not dumper:
		dumper = yaml.Dumper

	def construct_yaml_str(loader, node):
		s = loader.construct_scalar(node)
		return s.decode('utf-8')

	dumper.add_representer(str, construct_yaml_str)

	return dumper.dump(obj)
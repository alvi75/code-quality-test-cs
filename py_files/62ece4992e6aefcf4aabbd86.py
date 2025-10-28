def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""
	if not isinstance(obj, dict) and not isinstance(obj, list):
		return str(obj)
	else:
		dumper = yaml.Dumper if dumper is None else dumper
		stream = StringIO()
		dumper.stream = stream
		dumper.representers[datetime.datetime] = datetime_representer
		dumper.representers[str] = string_representer
		dumper.representers[int] = int_representer
		dumper.representers[float] = float_representer
		dumper.representers[bool] = bool_representer
		dumper.representers[type(None)] = null_representer
		dumper.representers[bytes] = bytes_representer
		dumper.representers[bytearray] = bytearray_representer
		dumper.representers[set] = set_representer
		dumper.representers[frozenset] = frozenset_representer
		dumper.representers[tuple] = tuple_representer
		dumper.representers[list] = list_representer
		dumper.representers[dict] = dict_representer
		dumper.representers[object] = object_representer
		dumper.representers[None] = null_representer
		dumper.ignore_aliases = True
		dumper.indent(sequence=4, mapping=2)
		dumper.default_flow_style = False
		dumper.dump(obj, stream)
		return stream.getvalue()
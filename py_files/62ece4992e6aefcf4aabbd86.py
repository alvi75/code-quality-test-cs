def _dump_string(obj, dumper=None):
	"""
	Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
	"""

	if not isinstance(obj, dict) and not hasattr(obj, '__iter__'):
		return str(obj)

	dump = yaml.dump_all if isinstance(obj, list) else yaml.dump
	stream = StringIO()
	dumper = dumper or yaml.Dumper
	dumper.ignore_aliases = lambda *args : False
	dumper.representer.add_representer(dict, lambda dumper, value : dump([value]))
	dumper.representer.add_representer(list, lambda dumper, value : dump(value))
	dumper.representer.add_representer(set, lambda dumper, value : dump(list(value)))
	dumper.representer.add_representer(tuple, lambda dumper, value : dump(list(value)))

	try:
		dumper.representers[datetime.datetime] = datetime_datetime_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[datetime.date] = datetime_date_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[datetime.time] = datetime_time_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[decimal.Decimal] = decimal_decimal_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[int] = int_int_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[float] = float_float_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[str] = str_str_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[bool] = bool_bool_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[type(None)] = None_none_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[uuid.UUID] = uuid_uuid_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[bytes] = bytes_bytes_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[bytearray] = bytearray_bytearray_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[MemoryView] = memoryview_memoryview_dumper
	except AttributeError:
		pass

	try:
		dumper.representers[io.IOBase] = io_io_base_d
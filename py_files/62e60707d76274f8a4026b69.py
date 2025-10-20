def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	def __init__(self, *args, **kwargs):
		super(Point, self).__init__(*args, **kwargs)
		self._fields = fields
		for field in fields:
			setattr(self, field.name, None)

	def _set_field(self, name, value):
		if name not in self._fields:
			raise ValueError("Field %s is not defined" % name)
		field = self._fields[name]
		value = field.type(value)
		setattr(self, name, value)

	def _get_field(self, name):
		return getattr(self, name)

	def _to_dict(self):
		dict_ = {}
		for field in self._fields.values():
			name = field.name
			value = getattr(self, name)
			if isinstance(field.type, list) or isinstance(field.type, tuple):
				value = [v for v in value if v is not None]
			elif isinstance(field.type, dict):
				value = {k: v for k, v in value.items() if v is not None}
			else:
				value = value
			dict_[name] = value
		return dict_

	def _from_dict(cls, d):
		obj = cls()
		for key, val in d.items():
			if key in obj._fields.keys():
				obj._set_field(key, val)
		return obj

	point_class = type(name, (Point,), {
		'__init__': __init__,
		'_set_field': _set_field,
		'_get_field': _get_field,
		'_to_dict': _to_dict,
		'_from_dict': _from_dict,
	})
	srid_map[point_class] = True
	return point_class
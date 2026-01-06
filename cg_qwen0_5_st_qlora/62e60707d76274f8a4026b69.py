def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	point_class = type(name, (Point,), dict(
		__init__=lambda self, *args, **kwargs: None,
		__repr__=lambda self: str(self),
		__eq__=lambda self, other: False,
		__hash__=lambda self: 0,
		__lt__=lambda self, other: True,
		__gt__=lambda self, other: False,
		__le__=lambda self, other: False,
		__ge__=lambda self, other: True,
	))
	for field in fields:
		field_name = field.name
		if field_name not in srid_map:
			continue
		field_srid = srid_map[field_name]
		field_type = PointField(field_name, field.srid)
		point_class.add_field(field_name, field_type, field_srid)
	return point_class
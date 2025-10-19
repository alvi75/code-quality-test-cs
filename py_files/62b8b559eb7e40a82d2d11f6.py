def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc

	metaclasses = [x.__class__ for x in bases]
	if len(metaclasses) == 0:
		return object
	elif len(metaclasses) == 1:
		return metaclasses[0]
	else:
		return type("MultiMetaclass", tuple(metaclasses), {})
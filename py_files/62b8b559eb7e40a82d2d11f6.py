def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if not bases:
		raise TypeError("No bases provided")
	mc = None
	for base in bases:
		mc = getattr(base, "__metaclass__", mc)
	if mc is None:
		return explicit_mc
	elif isinstance(mc, type):
		return mc
	else:
		raise TypeError("Invalid metaclass %r" % (mc,))
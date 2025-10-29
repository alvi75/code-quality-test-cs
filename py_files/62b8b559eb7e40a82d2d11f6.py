def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if not isinstance(bases, tuple):
		bases = (bases,)
	if len(bases) == 0:
		return object
	elif len(bases) == 1:
		return bases[0]
	else:
		mc = bases[-1]
		if mc.__metaclass__ is None:
			if explicit_mc is not None:
				return explicit_mc
			else:
				return type(mc)
		else:
			return mc
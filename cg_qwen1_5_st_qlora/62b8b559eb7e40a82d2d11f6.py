def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if not bases:
		return None

	mc = bases[0].__dict__.get('__metaclass__', None)
	if mc is not None:
		return mc

	if explicit_mc is not None:
		return explicit_mc

	if len(bases) == 1:
		return bases[0]

	for base in bases:
		mc = getattr(base, '__metaclass__', None)
		if mc is not None:
			return mc

	raise TypeError("No metaclass found for %s" % bases)
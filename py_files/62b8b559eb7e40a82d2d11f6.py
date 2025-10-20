def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if explicit_mc is not None:
		return explicit_mc

	if len(bases) == 0:
		raise TypeError("Cannot create a metaclass outside of a class hierarchy")

	if len(bases) == 1:
		return bases[0]

	mc = bases[-1]
	bases = bases[:-1]

	for base in bases:
		if isinstance(base, type):
			mc = _determineMetaclass(mc, base)
		else:
			mc = _determineMetaclass(mc, base.__class__)

	return mc